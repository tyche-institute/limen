#!/usr/bin/env python3
"""Generate print-oriented LIMEN preprint figures."""

from __future__ import annotations

import csv
import html
import math
import subprocess
from collections import Counter
from pathlib import Path
from textwrap import wrap


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "accelerated-submission" / "figures"

INK = "#111111"
MID = "#4b5563"
PALE = "#f4f6f8"
LINE = "#b8c0cc"
BLUE = "#174a7c"
GRAY = "#6b7280"
LIGHT_BAR = "#e5e9ef"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def text(lines: list[str], x: int, y: int, value: object, cls: str = "label", anchor: str = "start", color: str | None = None) -> None:
    extra = f' text-anchor="{anchor}"'
    if color:
        extra += f' fill="{color}"'
    lines.append(f'<text x="{x}" y="{y}" class="{cls}"{extra}>{esc(value)}</text>')


def wrapped(lines: list[str], x: int, y: int, value: str, width: int, cls: str = "small", step: int = 32) -> int:
    cur = y
    for part in wrap(value, width=width, break_long_words=False):
        text(lines, x, cur, part, cls=cls)
        cur += step
    return cur


def rect(lines: list[str], x: int, y: int, w: int, h: int, fill: str = "#ffffff", stroke: str = LINE, rx: int = 0, sw: int = 2) -> None:
    lines.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def line(lines: list[str], x1: int, y1: int, x2: int, y2: int, color: str = INK, sw: int = 3) -> None:
    lines.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"/>')


def svg_start(width: int, height: int, title: str, subtitle: str = "") -> list[str]:
    lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        "<style>",
        "text{font-family:Arial,Helvetica,sans-serif;fill:#111111}",
        ".title{font-size:58px;font-weight:700}",
        ".subtitle{font-size:34px;fill:#4b5563}",
        ".head{font-size:36px;font-weight:700}",
        ".label{font-size:32px}",
        ".small{font-size:28px;fill:#4b5563}",
        ".tiny{font-size:24px;fill:#4b5563}",
        ".num{font-size:52px;font-weight:700}",
        ".huge{font-size:78px;font-weight:700}",
        "</style>",
        "</defs>",
        f'<rect width="{width}" height="{height}" fill="#ffffff"/>',
        f'<text x="70" y="82" class="title">{esc(title)}</text>',
    ]
    if subtitle:
        lines.append(f'<text x="70" y="132" class="subtitle">{esc(subtitle)}</text>')
    return lines


def save(name: str, lines: list[str]) -> Path:
    path = OUT / name
    path.write_text("\n".join(lines + ["</svg>\n"]), encoding="utf-8")
    return path


def render(path: Path) -> None:
    subprocess.run(["rsvg-convert", "-w", "2800", "-f", "png", "-o", str(path.with_suffix(".png")), str(path)], check=True)


def cases() -> list[dict[str, str]]:
    return read_tsv(ROOT / "review" / "full-case-review-20260607.tsv")


def scale_counts() -> dict[str, int]:
    return {row["layer"]: int(row["count"]) for row in read_tsv(ROOT / "exports" / "full-observatory-scale-summary.tsv")}


def figure1() -> None:
    rows = cases()
    scale = scale_counts()
    verdicts = Counter(row["review_verdict"] for row in rows)
    core = sum(1 for row in rows if row["paper_layer"] == "reviewed_core")
    data = [
        ("Discovery", scale["cpu_mining_latest_total"], "signals"),
        ("Link checks", scale["public_link_checks"], "checks"),
        ("Source anchors", scale["source_anchors"], "records"),
        ("Reviewed rows", len(rows), "rows"),
        ("Reviewed core", core, "rows"),
        ("Bounded examples", verdicts["ready_bounded_core"], "rows"),
        ("Limited core", verdicts["limited_core_keep_for_methods_or_coverage"], "rows"),
    ]
    lines = svg_start(1700, 880, "Evidence gradient", "Log-scaled bars; counts are evidence layers.")
    y0 = 220
    text(lines, 100, y0 - 45, "Layer", "head")
    text(lines, 455, y0 - 45, "Count", "head")
    text(lines, 745, y0 - 45, "Log scale", "head")
    line(lines, 90, y0 - 20, 1600, y0 - 20, INK, 4)
    max_log = math.log10(max(v for _, v, _ in data))
    for i, (label, count, unit) in enumerate(data):
        y = y0 + i * 88
        line(lines, 90, y + 32, 1600, y + 32, "#e1e5ea", 2)
        text(lines, 100, y, label, "label")
        text(lines, 455, y + 6, f"{count:,}", "num")
        text(lines, 620, y, unit, "small")
        rect(lines, 745, y - 31, 670, 34, LIGHT_BAR, LIGHT_BAR, rx=0, sw=1)
        w = int(670 * math.log10(count) / max_log)
        rect(lines, 745, y - 31, w, 34, BLUE, BLUE, rx=0, sw=1)
    rect(lines, 90, 805, 1510, 2, INK, INK, sw=1)
    text(lines, 100, 850, "The reviewed core is the paper denominator; discovery remains the operating surface.", "small")
    save("preprint-figure1-evidence-gradient.svg", lines)


def figure2() -> None:
    rows = read_tsv(ROOT / "exports" / "taxonomy-heatmap.tsv")
    official = sum(1 for row in rows if int(row["authoritative_seed_count"]) > 0)
    candidate = sum(1 for row in rows if int(row["seed_case_count"]) > 0 and int(row["authoritative_seed_count"]) == 0)
    zero = sum(1 for row in rows if int(row["seed_case_count"]) == 0)
    largest = sorted(
        ((row["category_label"], int(row["seed_case_count"]), int(row["authoritative_seed_count"])) for row in rows),
        key=lambda item: (item[1], item[2]),
        reverse=True,
    )[:4]
    zero_labels = [
        row["category_label"].replace("Health, medical, or mental-health misuse", "health / medical")
        .replace("Residual/unclassified", "residual")
        .lower()
        for row in rows
        if int(row["seed_case_count"]) == 0
    ]
    lines = svg_start(1700, 900, "Register scarcity", "Category support is uneven across the frozen snapshot.")
    bars = [("Official support", official), ("Candidate-only", candidate), ("Zero-seed gaps", zero)]
    max_v = max(v for _, v in bars)
    y = 235
    for label, value in bars:
        text(lines, 115, y + 5, label, "head")
        text(lines, 600, y + 14, value, "huge")
        rect(lines, 780, y - 42, 610, 42, LIGHT_BAR, LIGHT_BAR, sw=1)
        rect(lines, 780, y - 42, int(610 * value / max_v), 42, BLUE if label == "Official support" else GRAY, BLUE if label == "Official support" else GRAY, sw=1)
        y += 125
    line(lines, 90, 585, 1600, 585, INK, 4)
    text(lines, 115, 650, "Largest seeded categories", "head")
    for i, (label, seed, auth) in enumerate(largest):
        cleaned = label.replace("AI washing or false AI claim", "Artificial-intelligence washing or false claim")
        cleaned = cleaned.replace("Education, workplace, or HR", "Education, workplace, or hiring")
        text(lines, 115, 705 + i * 44, cleaned, "small")
        text(lines, 1150, 705 + i * 44, f"{seed} seeds / {auth} official", "small")
    text(lines, 115, 870, "Zero-seed rows: " + ", ".join(zero_labels) + ".", "small")
    save("preprint-figure2-register-scarcity.svg", lines)


def figure3() -> None:
    lifecycle = [row["action"].title() for row in read_tsv(Path("/srv/tyche/projects/limen-ai-edge-case-atlas/results/attestation/lifecycle-live-coverage-v0.1.tsv"))]
    controls = ["Source depth", "Access state", "Language state", "Duplicate state", "Claim limit"]
    lines = svg_start(1700, 880, "Workflow infrastructure versus event evidence", "Process receipts and event claims are separate axes.")
    text(lines, 150, 205, "Workflow receipts", "head")
    text(lines, 1010, 205, "Evidence controls", "head")
    line(lines, 110, 235, 735, 235, INK, 4)
    line(lines, 970, 235, 1545, 235, INK, 4)
    x = 160
    for i, label in enumerate(lifecycle):
        y = 310 + i * 76
        lines.append(f'<circle cx="{x}" cy="{y - 10}" r="15" fill="{BLUE}"/>')
        text(lines, x + 45, y, label, "label")
        if i < len(lifecycle) - 1:
            line(lines, x, y + 8, x, y + 45, LINE, 3)
    for i, label in enumerate(controls):
        y = 315 + i * 96
        rect(lines, 990, y - 43, 500, 56, "#ffffff", INK, sw=2)
        text(lines, 1018, y - 6, label, "label")
    text(lines, 150, 820, "Complete workflow records improve auditability.", "small")
    text(lines, 970, 820, "They do not upgrade weak public sources.", "small")
    save("preprint-figure3-lifecycle-infrastructure-contrast.svg", lines)


def figure4() -> None:
    lines = svg_start(1700, 880, "Comparator cohort", "Comparison systems have different evidence roles.")
    x0, y0 = 250, 700
    line(lines, x0, y0, 1450, y0, INK, 4)
    line(lines, x0, y0, x0, 210, INK, 4)
    lines.append(f'<polygon points="1450,{y0} 1418,{y0 - 18} 1418,{y0 + 18}" fill="{INK}"/>')
    lines.append(f'<polygon points="{x0},210 {x0 - 18},242 {x0 + 18},242" fill="{INK}"/>')
    text(lines, 520, 775, "More machine-readable", "small")
    text(lines, 100, 250, "Stronger event record", "small")
    points = [
        ("Enforcement\nrecords", 500, 330, "11"),
        ("Structured\nvulnerability\nrecords", 1050, 360, "8"),
        ("Public\nregisters", 640, 470, "2"),
        ("Incident\nmonitors", 835, 560, "2"),
        ("Risk\nvocabularies", 1080, 565, "2"),
    ]
    for label, x, y, count in points:
        lines.append(f'<circle cx="{x}" cy="{y}" r="56" fill="{BLUE}" opacity="0.92"/>')
        text(lines, x, y + 16, count, "num", anchor="middle", color="#ffffff")
        for j, part in enumerate(label.split("\n")):
            text(lines, x, y + 92 + j * 30, part, "tiny", anchor="middle")
    rect(lines, 245, 205, 1205, 495, "none", LINE, sw=2)
    save("preprint-figure4-comparator-cohort.svg", lines)


def figure5() -> None:
    scale = scale_counts()
    verdicts = Counter(row["review_verdict"] for row in cases())
    lanes = [
        ("Keep stable", "Reviewed core", 21),
        ("Promote carefully", "Candidate leads", scale["candidate_examples"]),
        ("Use as context", "Side anchors", 7),
        ("Check access", "Public links", scale["public_link_checks"]),
        ("Triage", "Discovery signals", scale["cpu_mining_latest_total"]),
        ("Hold", "Document pending", verdicts["hold_complex_chronology"] + verdicts["hold_document_read_pending"]),
    ]
    lines = svg_start(1700, 900, "Full-scale observatory operation", "The paper core stays fixed while the observatory continues to move.")
    cols = [(95, 230), (610, 230), (1125, 230), (95, 545), (610, 545), (1125, 545)]
    for (verb, noun, value), (x, y) in zip(lanes, cols):
        rect(lines, x, y, 420, 210, "#ffffff", INK, sw=3)
        text(lines, x + 30, y + 55, verb, "head")
        text(lines, x + 30, y + 105, noun, "label")
        text(lines, x + 30, y + 175, f"{value:,}", "huge")
    line(lines, 515, 335, 610, 335, LINE, 5)
    line(lines, 1030, 335, 1125, 335, LINE, 5)
    line(lines, 515, 650, 610, 650, LINE, 5)
    line(lines, 1030, 650, 1125, 650, LINE, 5)
    text(lines, 95, 835, "Operating rule: growth happens outside the locked reviewed-core denominator.", "small")
    save("preprint-figure5-workflow-bands.svg", lines)


def figure6() -> None:
    rows = cases()

    def flag_count(flag: str) -> int:
        return sum(1 for row in rows if flag in row["flags"].split(";"))

    data = [
        ("Anchor export gap", flag_count("no_authoritative_anchor_row_in_anchor_export")),
        ("Identifier collision", 9),
        ("Translation caution", flag_count("translation_caution")),
        ("Low confidence", flag_count("low_confidence_cap")),
        ("Access limit", flag_count("access_limit_recorded")),
        ("Document hold", flag_count("hold_candidate")),
    ]
    max_v = max(v for _, v in data)
    lines = svg_start(1700, 880, "Bridge stress-test counts", "Constraints are operating controls, not hidden footnotes.")
    y0 = 220
    for i, (label, value) in enumerate(data):
        y = y0 + i * 92
        text(lines, 115, y, label, "label")
        rect(lines, 610, y - 35, 720, 42, LIGHT_BAR, LIGHT_BAR, sw=1)
        rect(lines, 610, y - 35, int(720 * value / max_v), 42, BLUE, BLUE, sw=1)
        text(lines, 1385, y + 3, value, "num")
    line(lines, 95, 790, 1520, 790, INK, 4)
    text(lines, 115, 835, "Next cycle: synchronize, read held records, triage discovery, and refresh the dashboard.", "small")
    save("preprint-figure6-bridge-stress-test.svg", lines)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    figure1()
    figure2()
    figure3()
    figure4()
    figure5()
    figure6()
    for svg in sorted(OUT.glob("preprint-figure*.svg")):
        render(svg)
        print(svg.name)


if __name__ == "__main__":
    main()
