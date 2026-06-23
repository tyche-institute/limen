#!/usr/bin/env bash
# Build the DOUBLE-BLIND (anonymized) LIMEN preprint v0.2 PDF.
# Source of truth = preprint-v0.2-anon.md (no author/affiliation, no system name,
# no companion URL, anon figure). Re-run after editing the markdown.
set -euo pipefail
cd "$(dirname "$0")"

SRC="preprint-v0.2-anon.md"
BUILD="/tmp/limen-preprint-v0.2-anon.build.md"
OUT="preprint-v0.2-anon.pdf"

# Lift the leading title block (down to the first '---' rule) into pandoc YAML metadata.
# Deliberately NO author field — this is the blind copy.
python3 - "$SRC" "$BUILD" <<'PY'
import sys
src=open(sys.argv[1]).read()
marker="\n---\n"
body=src[src.find(marker)+len(marker):]
yaml='''---
title: "A reviewer-safe public-source observatory for AI edge cases under source, language, and governance uncertainty"
date: "Methods/data article · preprint draft v0.2 · double-blind submission — author and affiliation withheld for review"
---

'''
open(sys.argv[2],"w").write(yaml+body)
PY

pandoc "$BUILD" -o "$OUT" \
  --pdf-engine=xelatex \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V linestretch=1.08 \
  -V mainfont="TeX Gyre Pagella" \
  -V sansfont="TeX Gyre Heros" \
  -V monofont="DejaVu Sans Mono" \
  -V colorlinks=true -V linkcolor=NavyBlue -V urlcolor=NavyBlue \
  -V title-meta="Reviewer-safe AI edge-case observatory (blind)" \
  -V author-meta="Anonymous" \
  --toc --toc-depth=2

echo "wrote $OUT"
