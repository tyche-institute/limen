#!/usr/bin/env python3
"""Materialize Claude adjudication into standard source-review batch dirs.

Reuses validate_batch from source_review_lane.py so output is byte-compatible
with the existing drain pipeline / ledger (completed_ids scans results.tsv).
"""
import csv, json, importlib.util
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone

PROJ = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
ROOT = PROJ/"results"/"review-candidates"
BATCH = ROOT/"source-review-batches"
TARGET = Path(ROOT/"source-review-drain-targets/current-target.txt").read_text().strip()
RESULT_FIELDS = ["signal_id","source_review_verdict","source_review_role","reason","claim_ceiling","next_action","source_path"]

# import the lane module to reuse validate_batch
spec = importlib.util.spec_from_file_location("srl", PROJ/"tools"/"source_review_lane.py")
srl = importlib.util.module_from_spec(spec); spec.loader.exec_module(srl)

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
def stamp(): return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

adj = {r["signal_id"]:r for r in csv.DictReader(open(ROOT/"claude-adjudication.tsv",encoding="utf-8"),delimiter="\t")}
queue_rows = list(csv.DictReader(open(TARGET,encoding="utf-8"),delimiter="\t"))
remaining = [r for r in queue_rows if r["signal_id"] in adj]   # original full-column rows, queue order
qfields = list(queue_rows[0].keys())
S = stamp()
N = 100
batches = [remaining[i:i+N] for i in range(0, len(remaining), N)]
print(f"materializing {len(remaining)} rows into {len(batches)} batches")

total = Counter(); made=0
for idx, chunk in enumerate(batches, 1):
    bid = f"{S}-claude{idx:02d}"
    bdir = BATCH/bid; bdir.mkdir(parents=True, exist_ok=True)
    # input.tsv (full original columns)
    with (bdir/"source-review-input.tsv").open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,delimiter="\t",fieldnames=qfields,extrasaction="ignore"); w.writeheader(); w.writerows(chunk)
    # results.tsv (RESULT_FIELDS exact)
    res=[]
    for r in chunk:
        a=adj[r["signal_id"]]
        res.append({k:(a.get(k,"") or "").replace("\t"," ").replace("\n"," ") for k in RESULT_FIELDS})
    with (bdir/"source-review-results.tsv").open("w",encoding="utf-8",newline="") as fh:
        w=csv.DictWriter(fh,delimiter="\t",fieldnames=RESULT_FIELDS,extrasaction="ignore"); w.writeheader(); w.writerows(res)
    counts = Counter(x["source_review_verdict"] for x in res)
    # summary.md
    (bdir/"source-review-summary.md").write_text(
        f"# Source-review batch {bid}\n\n- rows reviewed: {len(res)}\n- reviewer: claude-opus-4-8 (rerouted from stalled codex lanes)\n"
        f"- verdict counts:\n" + "".join(f"  - {k}: {v}\n" for k,v in sorted(counts.items())) +
        "\n## Boundary\nSource-surface triage only, local metadata/files only. No incident-truth, legality, "
        "compliance, safety, deployment, prevalence, or ranking claim. No crawling/external action.\n\n"
        "## Next smallest queue-hardening move\nExtract named source surfaces from the needs_named_source_extraction rows.\n",
        encoding="utf-8")
    # validate using the worker's own validator
    ok, reason, vc = srl.validate_batch(bdir)
    manifest = {
        "batch_id": bid, "batch_size": N, "created_at_utc": now(), "completed_at_utc": now(),
        "input": str(bdir/"source-review-input.tsv"), "input_rows": len(chunk), "lane_id": "claude",
        "queue": TARGET, "queue_rows": len(queue_rows),
        "results": str(bdir/"source-review-results.tsv"), "summary": str(bdir/"source-review-summary.md"),
        "status": "complete" if ok else "failed",
        "reviewed_by": "claude-opus-4-8", "provider": "anthropic-claude",
        "adjudication_method": "claude-authored rubric classifier (tools/claude_source_review_classify.py) with audited samples; conservative hold-to-ceiling on promotions",
        "verdict_counts": dict(sorted(vc.items())), "verified_row_count": len(res),
        "verified_signal_id_set_match": ok, "validation_reason": reason, "updated_at_utc": now(),
    }
    (bdir/"manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    (bdir/"source-review-prompt.md").write_text(f"Claude reroute adjudication for {bid}; see tools/claude_source_review_classify.py\n",encoding="utf-8")
    if not ok:
        print(f"  !! batch {bid} FAILED validation: {reason}"); 
    else:
        made+=1
    total.update(counts)

print(f"\nbatches complete: {made}/{len(batches)}")
print("verdict totals across claude drain:")
for k,v in total.most_common(): print(f"  {v:5d}  {k}")
json.dump({"stamp":S,"rows":len(remaining),"batches":len(batches),"complete":made,"verdicts":dict(total)}, open("/tmp/limen_drain_result.json","w"))
