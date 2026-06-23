#!/usr/bin/env python3
"""Consolidate canonical curated edge-case sets into reviewed-core.

Honest promotion only: every record already exists as a curated reviewed case in
the project's own canonical case sets, each T2/T3 with a public-record anchor and
explicit claim ceiling. We normalize to the reviewed-core schema, namespace the
case_ids (the canonical files reuse LIMEN-0000XX across domains), and carry each
record's own limitation as verification_gap. No incidents invented; security set
is already surfaced via security-agentic-watch and is not duplicated here.
"""
import csv, json
from pathlib import Path

ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
HEADER = ["case_id","cve_id","record_status","evidence_tier","title","primary_source_id",
          "primary_source_url","access_date","language","jurisdiction","ai_system_type",
          "autonomy_level","impact_surface","limen_categories","mitre_atlas_mapping",
          "avid_mapping","owasp_llm_agentic_mapping","severity","mitigation_or_response",
          "paper_use_note","verification_gap"]

def jl(p):
    p=ROOT/p
    return [json.loads(l) for l in open(p,encoding="utf-8") if l.strip()] if p.exists() else []
def tv(p):
    p=ROOT/p
    return list(csv.DictReader(open(p,encoding="utf-8"),delimiter="\t")) if p.exists() else []

out=[]; seen=set()
def row(case_id,title,status,tier,juris,lang,ai_type,auton,cats,src_id,src_url,date,claim,gap,key,cve=""):
    if key in seen or not title: return
    seen.add(key)
    out.append({**{h:"" for h in HEADER},
        "case_id":case_id,"cve_id":cve,"record_status":status,"evidence_tier":tier,"title":title,
        "primary_source_id":src_id,"primary_source_url":src_url,"access_date":date,"language":lang,
        "jurisdiction":juris,"ai_system_type":ai_type,"autonomy_level":auton,
        "impact_surface":"legal/regulatory/research-integrity","limen_categories":cats,
        "paper_use_note":claim,"verification_gap":gap})

# --- canonical authoritative set (all T3) ---
for r in jl("data/cases/authoritative-candidates.jsonl"):
    cid=r.get("case_id","")
    sc=(r.get("source_claims") or [{}])[0]
    sctx=r.get("system_context") or {}
    ait=sctx.get("ai_system_type") or []
    juris="; ".join(r.get("jurisdictions") or [])
    lang="; ".join(r.get("languages") or [])
    cls=r.get("classification") or {}
    cats=";".join(cls.get("limen_categories") or cls.get("categories") or []) if isinstance(cls,dict) else (cls if isinstance(cls,str) else "")
    ed=r.get("event_dates") or {}
    key="garante" if "ChatGPT" in r.get("title","") and "Italian" in r.get("title","") else cid+"|auth"
    row(f"LIMEN-AUTH-{cid.split('-')[-1]}", r.get("title",""), r.get("record_status",""),
        r.get("evidence_tier",""), juris, lang, ";".join(ait) if isinstance(ait,list) else str(ait),
        sctx.get("autonomy_level",""), cats or "public_sector_misuse_or_gap",
        sc.get("source_id",""), sc.get("source_url","") or sc.get("url",""),
        (ed.get("reported_on") or ed.get("occurred_on") or "")[:10],
        r.get("summary",""), "; ".join(r.get("legal_normative_notes") or []) if isinstance(r.get("legal_normative_notes"),list) else (r.get("legal_normative_notes") or ""),
        key)

# --- procedural research-integrity cases not in the authoritative set ---
for i,r in enumerate(tv("results/dashboard-paper/procedural-contamination-source-depth-panel-v0.1.tsv"),1):
    b=(r.get("case_key_or_bucket","") or "").upper()
    if "GARANTE" in b or "WEAK_RESIDUAL" in b or b=="": continue  # Garante already in authoritative
    if "YLE" in b: t="Yle automated-content correction matter (Finland)"
    elif "SAGE" in b and "CHATGPT" in b: t="SAGE / ChatGPT fabricated-reference correction (research integrity)"
    elif "NEJM" in b: t="NEJM AI-imagery publisher notice (research integrity)"
    elif "SPRINGER-BOOK" in b: t="Springer book fabricated-citations notice (research integrity)"
    elif "SPRINGER-ICM" in b: t="Springer ICM fabricated-references notice (research integrity)"
    else: continue
    sds=r.get("source_depth_state","")
    tier="T3_authoritative_source" if "regulator_order" in sds or "document_grade" in sds else "T2_direct_notice_or_mediated"
    row(f"LIMEN-PROC-{i:03d}", t, "publisher_or_regulator_notice", tier,
        r.get("jurisdiction_scope",""), "", "", "", "legal_procedural_contamination",
        "", "", "", r.get("publication_safe_claim",""), r.get("publication_safe_limitation",""), b.lower())

with (ROOT/"results/security/limen-reviewed-core-extension-v0.1.tsv").open("w",encoding="utf-8",newline="") as fh:
    w=csv.DictWriter(fh,delimiter="\t",fieldnames=HEADER); w.writeheader(); w.writerows(out)
print(f"reviewed-core extension records: {len(out)}")
for r in out: print(f"  {r['case_id']:18s} [{r['evidence_tier'][:3]}] {r['jurisdiction'][:16]:16s} | {r['title'][:54]}")
