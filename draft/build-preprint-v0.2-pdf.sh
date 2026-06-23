#!/usr/bin/env bash
# Build the LIMEN preprint v0.2 PDF from draft/preprint-v0.2.md.
# Source of truth = preprint-v0.2.md; this script only assembles the PDF
# (YAML title block + pandoc/xelatex). Re-run after editing the markdown.
set -euo pipefail
cd "$(dirname "$0")"

SRC="preprint-v0.2.md"
BUILD="/tmp/limen-preprint-v0.2.build.md"
OUT="preprint-v0.2.pdf"

# Lift the leading title block (down to the first '---' rule) into pandoc YAML metadata.
python3 - "$SRC" "$BUILD" <<'PY'
import sys
src=open(sys.argv[1]).read()
marker="\n---\n"
body=src[src.find(marker)+len(marker):]
yaml='''---
title: "LIMEN: a reviewer-safe public-source observatory for AI edge cases under source, language, and governance uncertainty"
author: "Anton Sokolov · Tyche Institute"
date: "Preprint draft v0.2 — 2026-06-14 · Methods/data article · Live observatory: https://limen.eatf.eu · Public atlas: https://obscure-ai.eatf.eu"
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
  -V title-meta="LIMEN preprint v0.2" \
  --toc --toc-depth=2

echo "wrote $OUT"
