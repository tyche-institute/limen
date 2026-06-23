#!/usr/bin/env python3
"""Claude-authored adjudication of the LIMEN direct-source review queue remainder.

Rubric encoded from /tools/source_review_lane.py prompt. Priority order matters.
Output: claude-adjudication.tsv with RESULT_FIELDS + matched_rule + confidence for audit.
"""
import csv, json, re
from pathlib import Path
from collections import Counter

ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas/results/review-candidates")
TARGET = Path(ROOT/"source-review-drain-targets/current-target.txt").read_text().strip()
ids = set(json.load(open("/tmp/limen_remaining_ids.json")))
rows = [r for r in csv.DictReader(open(TARGET,encoding="utf-8"),delimiter="\t") if r["signal_id"] in ids]

NEG = re.compile(r'\bno official\b|\bnot found\b|\bno public\b|\bno central public\b|no .{0,30}register found|'
                 r'\bno evidence\b|could not find|search.?negative|\bno results?\b|none found|'
                 r'weak.?source|gap.?flag|absence of|no .{0,20}sandbox|no .{0,20}authority|'
                 r'not .{0,15}available|\bno ai\b.{0,25}found', re.I)
# internal/derived project artifacts that should not stay in a *direct-source* queue
NOISE_PATH = re.compile(r'/results/boost/|limen-boost|/program/|claim-defense|caption-control|'
                        r'/analysis/matrices/|standards-to-evidence|/next\.md$|/RESULT\.md$|'
                        r'\.(py|sh)$|/dashboard-paper/|/manuscript|/thesis|/draft/|claims\.md$|'
                        r'crosswalk\.tsv$|denominator-eligibility|backups?-cycle', re.I)
NOISE_SNIP = re.compile(r'\| Indicator |scoring rule|heuristic split|bundle caption|manuscript/dashboard', re.I)
# concrete external source surface
URL = re.compile(r'https?://[^\s,"]+', re.I)
NAMED_SURFACE = re.compile(r'\b(register|registry|regulator|authority|court|tribunal|gazette|'
                           r'procurement|notice|advisory|bulletin|decision|ruling|enforcement|'
                           r'supervisor|commission|ministry|agency)\b', re.I)
# already-modeled local registry surfaces -> merge (conservative: explicit known registers)
MERGE = re.compile(r'Helsinki AI Register|Amsterdam .{0,12}Register|Scottish AI Register|'
                   r'algorithm ?register .{0,20}(active_register|listing_snippet)', re.I)

def nonascii_ratio(s):
    letters=[c for c in s if c.isalpha()]
    return sum(1 for c in letters if ord(c)>127)/len(letters) if letters else 0

def classify(r):
    sn = r.get("snippet","") or ""
    qr = r.get("queue_reason","") or ""
    sp = r.get("source_path","") or ""
    role = r.get("candidate_role","")
    text = sn+" "+qr
    extURL = [u for u in URL.findall(sn) if not re.search(r"eatf\.eu|tyche|zenodo\.org", u, re.I)]
    # drop third-party search engines / text proxies: not direct source surfaces
    extURL = [u for u in extURL if not re.search(r"r\.jina\.ai|duckduckgo|google\.[a-z]+/search|\bbing\.com", u, re.I)]
    is_source_pack = re.search(r"SOURCE_PACK|SOURCE_REFRESH|SOURCE_CANDIDATES|acquisition-queue|SECOND_PASS_SPRINT_\d+_SOURCE", sp, re.I)
    ext_snapshot = bool(re.search(r"/snapshots/.+\.bin$", sp)) and bool(re.search(r"https?://", sn))

    # 1 negative evidence
    if NEG.search(text):
        return ("negative_evidence_candidate","negative_search",
                "Local source/search summary records a negative or absence result.",
                "negative evidence only from bounded local review","keep as bounded gap evidence","rule")
    # 2 internal prose / methodology / script / our own site-build / manuscript -> reject_noise
    if NOISE_PATH.search(sp) or NOISE_SNIP.search(sn):
        return ("reject_noise","internal_artifact",
                "Internal LIMEN/atlas working artifact (boost/methodology/manuscript/preprint/notes/site-build/script), not a direct source surface.",
                "no claim; queue-hygiene only","drop from direct-source queue","rule")
    # 3 translation
    if nonascii_ratio(sn) > 0.15:
        return ("translation_review_needed","non_english_surface",
                "Row names a plausible source surface but local evidence is materially non-English.",
                "source-surface existence pending translation","route to translation-aware review","rule")
    # 4 patents / cross-topic -> hold for extraction (do not promote, do not claim)
    if re.search(r"epo-ops|patentscope|patent-index|\bWO_?\d{6,}|combined-patent", sp+" "+sn, re.I):
        return ("needs_named_source_extraction","cross_topic_patent",
                "Patent/cross-topic row points to an external record but is outside the LIMEN direct-source surface scope here.",
                "source-surface existence only from local metadata","extract/route the named source if in scope","rule")
    # 5 internal aggregates/corpus/exports that merely cite a source -> hold for extraction
    if re.search(r"gaia-records|atlas-facts|global-agent-atlas|eu-agent-atlas|/corpus/|combined-patent-index|/sources/sources\.md$", sp, re.I):
        return ("needs_named_source_extraction","internal_aggregate",
                "Internal corpus/atlas aggregate cites a source but does not expose a standalone reviewable source surface row.",
                "source-surface existence only from local metadata/files","extract the named source surface from the aggregate","rule")
    # 6 already-modeled registry surface -> merge (conservative)
    if MERGE.search(sn) or re.search(r"ai\.hel\.fi", sp+sn, re.I):
        return ("merge_existing_surface","modeled_registry_listing",
                "Row duplicates an already-modeled local registry/atlas surface and should be deduplicated.",
                "no new surface; dedupe only","merge into existing modeled registry surface","rule")
    # 7 genuine external source-pack listing: named authority + external URL -> reviewed candidate
    if extURL and (is_source_pack or NAMED_SURFACE.search(sn)) and is_source_pack:
        return ("source_reviewed_candidate","direct_surface",
                "Source-pack listing pairs a named external authority/source with a direct external URL.",
                "source-surface existence only from local metadata","open bounded direct source review packet","rule")
    if ext_snapshot and NAMED_SURFACE.search(sn):
        return ("source_reviewed_candidate","external_snapshot",
                "Locally cached external page snapshot exposes a named source surface.",
                "source-surface existence only from local snapshot","open bounded direct source review packet","rule")
    # 8 default: points toward a source but no standalone named reviewable surface yet
    return ("needs_named_source_extraction","source_pack_proxy",
            "Source-pack/index/profile row points toward a source but does not expose a named reviewable surface.",
            "source-surface existence only from local metadata/files","extract the named source surface from local materials","rule")

out=[]
for r in rows:
    v,role,reason,ceil,nxt,conf = classify(r)
    reason=reason.replace("\t"," ").replace("\n"," ")
    out.append({"signal_id":r["signal_id"],"source_review_verdict":v,"source_review_role":role,
                "reason":reason,"claim_ceiling":ceil,"next_action":nxt,
                "source_path":(r.get("source_path","") or "").replace("\t"," "),
                "matched_confidence":conf})

ADJ = ROOT/"claude-adjudication.tsv"
with ADJ.open("w",encoding="utf-8",newline="") as fh:
    w=csv.DictWriter(fh,delimiter="\t",fieldnames=["signal_id","source_review_verdict","source_review_role","reason","claim_ceiling","next_action","source_path","matched_confidence"])
    w.writeheader(); w.writerows(out)

print("total adjudicated:", len(out))
for k,v in Counter(o["source_review_verdict"] for o in out).most_common(): print(f"  {v:5d}  {k}")
print("wrote", ADJ)
