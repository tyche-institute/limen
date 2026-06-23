#!/usr/bin/env python3
"""Generate plain-language LIMEN paper figures from the frozen TSV exports."""

from __future__ import annotations

import csv
import html
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT.parents[1]
OUT = ROOT / "accelerated-submission" / "figures"

INK = "#172033"
MUTED = "#526071"
GRID = "#d7dde8"
BG = "#ffffff"
PANEL = "#f7f9fc"
BLUE = "#2166ac"
GREEN = "#188b5b"
AMBER = "#c97700"
RED = "#c43c39"
PURPLE = "#6b4cb4"
TEAL = "#087f8c"
GRAY = "#667085"


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def count_rows(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8") as f:
        return max(sum(1 for _ in f) - 1, 0)


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def wrap(text: str, width: int) -> list[str]:
    words = str(text).replace("_", " ").split()
    lines: list[str] = []
    cur: list[str] = []
    for word in words:
        trial = " ".join(cur + [word])
        if len(trial) <= width or not cur:
            cur.append(word)
        else:
            lines.append(" ".join(cur))
            cur = [word]
    if cur:
        lines.append(" ".join(cur))
    return lines


def svg_start(width: int, height: int, title: str, subtitle: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        "<style>",
        "text{font-family:Arial,Helvetica,sans-serif;fill:#172033}",
        ".title{font-size:46px;font-weight:700}",
        ".subtitle{font-size:28px;fill:#526071}",
        ".section{font-size:29px;font-weight:700}",
        ".label{font-size:27px}",
        ".small{font-size:22px;fill:#526071}",
        ".tiny{font-size:18px;fill:#526071}",
        ".number{font-size:40px;font-weight:700}",
        "</style>",
        "</defs>",
        f'<rect width="{width}" height="{height}" fill="{BG}"/>',
        f'<text x="60" y="70" class="title">{esc(title)}</text>',
        f'<text x="60" y="108" class="subtitle">{esc(subtitle)}</text>',
    ]


def save(name: str, lines: list[str]) -> None:
    (OUT / name).write_text("\n".join(lines + ["</svg>\n"]), encoding="utf-8")


def note(lines: list[str], y: int, text: str, width: int = 1680) -> None:
    for i, line in enumerate(wrap(text, 150)):
        lines.append(f'<text x="60" y="{y + i * 24}" class="tiny">{esc(line)}</text>')


def bar(lines: list[str], x: int, y: int, width: int, height: int, value: int, max_value: int, color: str) -> int:
    w = int(width * value / max(max_value, 1))
    lines.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="8" fill="#edf1f7"/>')
    lines.append(f'<rect x="{x}" y="{y}" width="{w}" height="{height}" rx="8" fill="{color}"/>')
    return w


def source_family_plain(name: str) -> str:
    mapping = {
        "Regulator and enforcement sources": "Regulators and enforcement agencies",
        "Court and tribunal records": "Courts and tribunal records",
        "Security research and advisories": "Security advisories and research",
        "Reputable multilingual media and investigations": "Local-language news and investigations",
        "Public-sector registers and procurement": "Public-sector registers and procurement",
        "Academic and research-integrity sources": "Research-integrity and publisher notices",
    }
    return mapping.get(name, name.replace("_", " "))


def figure1() -> None:
    scale_rows = {r["layer"]: r for r in read_tsv(ROOT / "exports" / "full-observatory-scale-summary.tsv")}
    cases = read_tsv(ROOT / "exports" / "cases.tsv")
    core = sum(1 for r in cases if r["snapshot_layer"] == "headline_denominator")
    side = len(cases) - core
    source_anchors = count_rows(ROOT / "exports" / "authoritative-source-anchors.tsv")
    public_checks = count_rows(ROOT / "exports" / "public-link-audit.tsv")
    source_families = count_rows(ROOT / "exports" / "source-families.tsv")
    categories = count_rows(ROOT / "exports" / "taxonomy-heatmap.tsv")
    candidate_examples = count_rows(ROOT / "exports" / "candidate-examples-table.tsv")
    lanes = [
        ("Public sector", "cpu_mining_public_sector"),
        ("Identity and provenance", "cpu_mining_identity_provenance"),
        ("Legal research", "cpu_mining_legal_research"),
        ("Residual and weird", "cpu_mining_residual_weird"),
        ("Security and agentic", "cpu_mining_security_agentic"),
        ("Health, finance, education", "cpu_mining_health_finance_education"),
    ]
    lane_counts: list[tuple[str, int]] = []
    for label, layer in lanes:
        lane_counts.append((label, int(scale_rows[layer]["count"])))
    total_signals = int(scale_rows["cpu_mining_latest_total"]["count"])

    lines = svg_start(
        1800,
        1220,
        "Figure 1. LIMEN is a layered observatory",
        "The reviewed core sits inside a larger system for sources, candidates, links, and discovery.",
    )
    cards = [
        ("Reviewed core", core, "duplicate-controlled case threads", BLUE),
        ("Side anchors", side, "official or public records outside the main count", GREEN),
        ("Source anchors", source_anchors, "dated public records for paper use", TEAL),
        ("Public-link checks", public_checks, "retrieval and source-check rows", PURPLE),
        ("Source families", source_families, "kinds of public evidence tracked", AMBER),
        ("Watch categories", categories, "topic areas and gaps", RED),
    ]
    x0, y0 = 85, 170
    for i, (title, value, body, color) in enumerate(cards):
        col = i % 3
        row = i // 3
        x = x0 + col * 570
        y = y0 + row * 205
        lines.append(f'<rect x="{x}" y="{y}" width="500" height="155" rx="18" fill="{PANEL}" stroke="{GRID}" stroke-width="2"/>')
        lines.append(f'<text x="{x + 35}" y="{y + 64}" class="number" fill="{color}">{value:,}</text>')
        lines.append(f'<text x="{x + 150}" y="{y + 58}" class="section">{esc(title)}</text>')
        for j, line in enumerate(wrap(body, 38)[:2]):
            lines.append(f'<text x="{x + 150}" y="{y + 92 + j * 27}" class="small">{esc(line)}</text>')

    y = 605
    lines.append(f'<rect x="85" y="{y}" width="1630" height="315" rx="24" fill="#f1f6fb" stroke="{GRID}" stroke-width="2"/>')
    lines.append(f'<text x="125" y="{y + 72}" class="title">{total_signals:,} discovery signals</text>')
    lines.append(f'<text x="125" y="{y + 112}" class="subtitle">recorded public-source mining leads; not reviewed cases</text>')
    max_v = max(v for _, v in lane_counts) or 1
    for i, (label, value) in enumerate(lane_counts):
        yy = y + 155 + i * 34
        lines.append(f'<text x="125" y="{yy + 19}" class="small">{esc(label)}</text>')
        w = bar(lines, 500, yy, 900, 20, value, max_v, [GREEN, TEAL, BLUE, RED, PURPLE, AMBER][i])
        lines.append(f'<text x="{500 + w + 18}" y="{yy + 20}" class="small">{value:,}</text>')
    note(lines, 1035, "The large discovery layer is lead material. It shows where to triage next.", width=1600)
    save("figure1-observatory-scale-map.svg", lines)


def figure2() -> None:
    rows = read_tsv(ROOT / "exports" / "category-source-family-counts.tsv")
    families = [
        r for r in rows
        if r["count_dimension"] == "source_family"
        and r["scope"] in {"headline_denominator", "paper_anchor_additions"}
    ]
    main = [r for r in families if r["scope"] == "headline_denominator"]
    side = [r for r in families if r["scope"] == "paper_anchor_additions"]
    lines = svg_start(
        1800,
        1180,
        "Figure 2. What kind of public evidence is visible?",
        "The paper separates the main set from extra anchors instead of mixing everything into one count.",
    )
    x, y = 650, 180
    max_v = max(int(r["lineage_count"]) for r in families)
    lines.append(f'<text x="60" y="{y}" class="section">Main paper set</text>')
    palette = [BLUE, TEAL, AMBER, PURPLE, GREEN]
    for i, r in enumerate(main):
        yy = y + 55 + i * 82
        label = source_family_plain(r["value"])
        lines.append(f'<text x="80" y="{yy + 31}" class="label">{esc(label)}</text>')
        w = bar(lines, x, yy, 800, 36, int(r["lineage_count"]), max_v, palette[i % len(palette)])
        lines.append(f'<text x="{x + w + 22}" y="{yy + 30}" class="number">{esc(r["lineage_count"])}</text>')
    y2 = y + 55 + len(main) * 82 + 80
    lines.append(f'<text x="60" y="{y2}" class="section">Extra anchors kept outside the main count</text>')
    for i, r in enumerate(side):
        yy = y2 + 55 + i * 82
        label = source_family_plain(r["value"])
        lines.append(f'<text x="80" y="{yy + 31}" class="label">{esc(label)}</text>')
        w = bar(lines, x, yy, 800, 36, int(r["lineage_count"]), max_v, GRAY)
        lines.append(f'<text x="{x + w + 22}" y="{yy + 30}" class="number">{esc(r["lineage_count"])}</text>')
    note(lines, 1110, "Read this as a map of observability, not a map of how often artificial intelligence failures happen.")
    save("figure2-source-family-observability-map.svg", lines)


def figure3() -> None:
    counts = read_tsv(ROOT / "exports" / "category-source-family-counts.tsv")

    def count(dim: str, value: str) -> int:
        for row in counts:
            if row["scope"] == "headline_denominator" and row["count_dimension"] == dim and row["value"] == value:
                return int(row["lineage_count"])
        return 0

    cards = [
        ("Main case threads", 21, "locked for this paper", BLUE),
        ("Official or authoritative records", count("evidence_tier", "T3_authoritative_source") + count("evidence_tier", "T3_authoritative_source_direct_url_resolved"), "can support narrow descriptions", GREEN),
        ("Single-source leads", count("evidence_tier", "T1_single_public_source"), "kept mainly for limits and discovery", AMBER),
        ("High-use examples", count("confidence_cap", "high"), "safe for bounded paper examples", TEAL),
        ("Low-use examples", count("confidence_cap", "low"), "must stay cautious", RED),
        ("Need translation caution", count("translation_dependency", "translation_dependent"), "cannot be treated like English records", PURPLE),
    ]
    lines = svg_start(
        1800,
        1120,
        "Figure 3. How strong is the public evidence?",
        "The same set contains firm public records and weaker leads; the paper labels them differently.",
    )
    max_v = max(v for _, v, _, _ in cards)
    x0, y0 = 95, 185
    for i, (label, value, sub, color) in enumerate(cards):
        col = i % 2
        row = i // 2
        x = x0 + col * 840
        y = y0 + row * 250
        lines.append(f'<rect x="{x}" y="{y}" width="760" height="195" rx="18" fill="{PANEL}" stroke="{GRID}" stroke-width="2"/>')
        lines.append(f'<text x="{x + 35}" y="{y + 62}" class="number" fill="{color}">{value}</text>')
        lines.append(f'<text x="{x + 120}" y="{y + 58}" class="section">{esc(label)}</text>')
        for j, line in enumerate(wrap(sub, 48)):
            lines.append(f'<text x="{x + 120}" y="{y + 96 + j * 26}" class="small">{esc(line)}</text>')
        bar(lines, x + 35, y + 135, 680, 26, value, max_v, color)
    note(lines, 1010, "High-use does not mean legally settled. Low-use does not mean false. These labels tell readers how cautiously each example can be used.")
    save("figure3-evidence-tier-funnel.svg", lines)


def figure4() -> None:
    edges = read_tsv(ROOT / "exports" / "duplicate-graph.tsv")
    counts = Counter(edge["edge_type"] for edge in edges)
    cards = [
        ("Identifier collision", counts["identifier_collision_blocker"], "A working label was reused for distinct events.", RED),
        ("Similar, distinct events", counts["reviewed_not_duplicate"], "Rows can share a regulator, product family, or failure mode and still remain separate.", BLUE),
        ("Duplicate rows excluded", 7, "Derivative rows are held out of the reviewed-core count.", GREEN),
    ]
    lines = svg_start(
        1800,
        1040,
        "Figure 4. Why counting public artificial intelligence cases is hard",
        "The observatory records counting decisions before it reports totals.",
    )
    for i, (title, value, body, color) in enumerate(cards):
        x = 90 + i * 560
        y = 210
        lines.append(f'<rect x="{x}" y="{y}" width="500" height="520" rx="22" fill="{PANEL}" stroke="{color}" stroke-width="5"/>')
        lines.append(f'<circle cx="{x + 75}" cy="{y + 95}" r="52" fill="{color}"/>')
        lines.append(f'<text x="{x + 75}" y="{y + 108}" text-anchor="middle" fill="white" style="font-size:40px;font-weight:700">{value}</text>')
        for j, line in enumerate(wrap(title, 28)):
            lines.append(f'<text x="{x + 35}" y="{y + 195 + j * 34}" class="section">{esc(line)}</text>')
        for j, line in enumerate(wrap(body, 36)):
            lines.append(f'<text x="{x + 35}" y="{y + 300 + j * 31}" class="label">{esc(line)}</text>')
    lines.append(f'<text x="150" y="835" class="section">Counting rule</text>')
    note(lines, 885, "Merge rows only when they refer to the same case thread.")
    save("figure4-duplicate-collision-graph.svg", lines)


def status_color(state: str) -> str:
    if "authoritatively" in state:
        return GREEN
    if "candidate" in state:
        return AMBER
    if "zero" in state or "no local" in state:
        return RED
    return GRAY


def figure5() -> None:
    rows = read_tsv(ROOT / "exports" / "taxonomy-heatmap.tsv")
    rows = sorted(rows, key=lambda r: int(r.get("seed_case_count") or 0), reverse=True)
    lines = svg_start(
        1700,
        1450,
        "Figure 5. What kinds of cases are easy or hard to see?",
        "The heatmap shows support and gaps; it does not rank harm or legality.",
    )
    left, bar_x, top = 60, 570, 180
    max_v = max(int(r.get("seed_case_count") or 0) for r in rows) or 1
    lines.append(f'<text x="{left}" y="{top - 25}" class="small">Topic area</text>')
    lines.append(f'<text x="{bar_x}" y="{top - 25}" class="small">Visible case threads</text>')
    lines.append(f'<text x="1230" y="{top - 25}" class="small">Public-evidence state</text>')
    for i, row in enumerate(rows):
        y = top + i * 78
        label = (
            row.get("category_label") or row.get("category_code")
        ).replace("AI washing or false AI claim", "Artificial intelligence washing or false claim").replace(
            "Education, workplace, or HR", "Education, workplace, or human resources"
        )
        seeds = int(row.get("seed_case_count") or 0)
        auth = int(row.get("authoritative_seed_count") or 0)
        state = row.get("support_state", "unknown").replace("_", " ")
        for j, line in enumerate(wrap(label, 34)[:2]):
            lines.append(f'<text x="{left}" y="{y + 25 + j * 26}" class="label">{esc(line)}</text>')
        w = bar(lines, bar_x, y, 420, 36, seeds, max_v, status_color(row.get("support_state", "")))
        lines.append(f'<text x="{bar_x + w + 20}" y="{y + 32}" class="number">{seeds}</text>')
        lines.append(f'<text x="1030" y="{y + 31}" class="small">{auth} official</text>')
        for j, line in enumerate(wrap(state, 30)[:2]):
            lines.append(f'<text x="1230" y="{y + 24 + j * 25}" class="small">{esc(line)}</text>')
    note(lines, 1385, "Empty or thin rows are not failures of the paper. They show where public evidence is missing, blocked, translated, or too weak for strong claims.", width=1500)
    save("figure5-taxonomy-heatmap.svg", lines)


def depth_plain(raw: str) -> str:
    mapping = {
        "title_gloss_or_discovery_surface": "Title or discovery lead",
        "single_media_or_investigation_lead": "Single article or investigation",
        "official_project_or_register_page": "Official project or register page",
        "agency_press_or_summary_page": "Agency summary page",
        "regulator_record_or_order_pdf": "Regulator record or order",
        "charging_document_or_indictment_pdf": "Court filing or indictment",
        "direct_publisher_notice_text": "Publisher notice",
        "complaint_plus_final_order_package": "Complaint plus final order",
    }
    return mapping.get(raw, raw.replace("_", " "))


def source_depth_caption(depth_class: str) -> tuple[str, str]:
    mapping = {
        "title_gloss_or_discovery_surface": (
            "Discovery and translation triage",
            "Facts, law, attribution, prevalence",
        ),
        "single_media_or_investigation_lead": (
            "Local context and public salience",
            "Official action or legal conclusion",
        ),
        "official_project_or_register_page": (
            "Disclosure and governance context",
            "Impact, effectiveness, or legality",
        ),
        "agency_press_or_summary_page": (
            "Agency status and public allegations",
            "Court text or merits finding",
        ),
        "regulator_record_or_order_pdf": (
            "Order wording, remedies, and dates",
            "Prevalence or independent legal conclusion",
        ),
        "charging_document_or_indictment_pdf": (
            "Accusation-stage procedural status",
            "Guilt, liability, or final disposition",
        ),
        "direct_publisher_notice_text": (
            "The notice's stated retraction rationale",
            "Author intent or field-wide pattern",
        ),
        "complaint_plus_final_order_package": (
            "Complaint and order obligations",
            "Product truth or detector validity",
        ),
    }
    return mapping.get(depth_class, ("Narrow public-source description", "Broad unsupported conclusion"))


def figure6() -> None:
    rows = read_tsv(ROOT / "exports" / "source-depth-ladder.tsv")
    lines = svg_start(
        1700,
        1190,
        "Figure 6. Public sources do not all let us say the same thing",
        "The ladder shows why an official-looking source still needs a specific claim limit.",
    )
    x0, y0 = 60, 165
    step_h = 110
    colors = [GRAY, AMBER, TEAL, BLUE, GREEN, PURPLE, RED, "#0c7c99"]
    for i, row in enumerate(rows):
        y = y0 + i * step_h
        color = colors[i % len(colors)]
        lines.append(f'<rect x="{x0}" y="{y}" width="465" height="72" rx="14" fill="{color}"/>')
        lines.append(f'<text x="{x0 + 24}" y="{y + 47}" style="font-size:27px;font-weight:700;fill:#ffffff">{esc(depth_plain(row["depth_class"]))}</text>')
        lines.append(f'<line x1="{x0 + 232}" y1="{y + 72}" x2="{x0 + 232}" y2="{y + step_h - 12}" stroke="{GRID}" stroke-width="5"/>')
        support, limit = source_depth_caption(row["depth_class"])
        lines.append(f'<text x="585" y="{y + 26}" class="section">Can support</text>')
        for j, line in enumerate(wrap(support, 43)[:2]):
            lines.append(f'<text x="585" y="{y + 62 + j * 28}" class="label">{esc(line)}</text>')
        lines.append(f'<text x="1120" y="{y + 26}" class="section">Cannot support alone</text>')
        for j, line in enumerate(wrap(limit, 42)[:2]):
            lines.append(f'<text x="1120" y="{y + 62 + j * 28}" class="label">{esc(line)}</text>')
    note(lines, 1125, "A source can be public and official while still failing to support broad conclusions. The method records that limit instead of hiding it.", width=1500)
    save("figure6-source-depth-ladder.svg", lines)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    figure1()
    figure2()
    figure3()
    figure4()
    figure5()
    figure6()


if __name__ == "__main__":
    main()
