#!/usr/bin/env bash
# Build the F1000Research Method Article PDF from draft/preprint-v0.3-f1000.md.
# Markdown is the source of truth; re-run after edits.
set -euo pipefail
cd "$(dirname "$0")"

SRC="preprint-v0.3-f1000.md"
BUILD="/tmp/limen-preprint-v0.3.build.md"
OUT="preprint-v0.3-f1000.pdf"

python3 - "$SRC" "$BUILD" <<'PY'
import sys
src=open(sys.argv[1]).read()
marker="\n---\n"
body=src[src.find(marker)+len(marker):]
yaml='''---
title: "LIMEN: a reviewer-safe public-source observatory for AI edge cases under source, language, and governance uncertainty"
author: "Anton Sokolov · Tyche Institute, Tallinn, Estonia · ORCID 0000-0003-2452-7096"
date: "Method Article (prepared for F1000Research) · v0.3 · Live observatory: https://limen.eatf.eu · Public atlas: https://obscure-ai.eatf.eu"
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
  -V title-meta="LIMEN method article (F1000Research)" \
  -V author-meta="Anton Sokolov" \
  --toc --toc-depth=2

echo "wrote $OUT"
