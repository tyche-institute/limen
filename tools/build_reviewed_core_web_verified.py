#!/usr/bin/env python3
"""Web-verified reviewed-core edge cases (bounded external-verification pass).

Each record is a real AI edge case with a public-record anchor (regulator
decision, court ruling, or state-AG settlement) confirmed via web search on
2026-06-14. Tiers are conservative; appeals / settlements / review status are
recorded in verification_gap. No prevalence, no merits beyond the cited record.
"""
import csv
from pathlib import Path
ROOT = Path("/srv/tyche/projects/limen-ai-edge-case-atlas")
HEADER = ["case_id","cve_id","record_status","evidence_tier","title","primary_source_id",
          "primary_source_url","access_date","language","jurisdiction","ai_system_type",
          "autonomy_level","impact_surface","limen_categories","mitre_atlas_mapping",
          "avid_mapping","owasp_llm_agentic_mapping","severity","mitigation_or_response",
          "paper_use_note","verification_gap"]
AD="2026-06-14"
R=[
 dict(case_id="LIMEN-WEB-001",record_status="regulator_final",evidence_tier="T3_authoritative_source",
   title="Clearview AI fined by multiple EU DPAs for unlawful facial-recognition scraping",
   primary_source_id="EDPB national-news (FR/IT/EL) + Dutch AP",primary_source_url="https://www.edpb.europa.eu/news/national-news/2022/french-sa-fines-clearview-ai-eur-20-million_en",
   jurisdiction="France; Italy; Greece; Netherlands; United Kingdom",language="en",ai_system_type="facial_recognition",
   limen_categories="surveillance_biometrics_or_policing",
   paper_use_note="Multiple EU DPAs issued GDPR fines (FR EUR20M, IT EUR20M 2022-02, EL EUR20M, NL EUR30.5M) ordering deletion/cessation of biometric scraping.",
   verification_gap="Cross-border collection of separate national decisions; Clearview has largely not paid and contests jurisdiction; UK fine under appeal."),
 dict(case_id="LIMEN-WEB-002",record_status="tribunal_decision",evidence_tier="T3_authoritative_source",
   title="Moffatt v. Air Canada: airline liable for its chatbot's negligent misrepresentation",
   primary_source_id="2024 BCCRT 149 (BC Civil Resolution Tribunal)",primary_source_url="https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html",
   jurisdiction="Canada",language="en",ai_system_type="customer_service_chatbot",autonomy_level="content_only",
   limen_categories="agentic_control_failure",
   paper_use_note="Tribunal (2024-02-14) found Air Canada liable for negligent misrepresentation by its website chatbot; awarded CAD 650.88.",
   verification_gap="Small-claims tribunal decision; not appellate precedent."),
 dict(case_id="LIMEN-WEB-003",record_status="court_sanction_order",evidence_tier="T3_authoritative_source",
   title="Mata v. Avianca: Rule 11 sanctions for ChatGPT-fabricated case citations",
   primary_source_id="678 F.Supp.3d 443 (S.D.N.Y. 2023), Castel J.",primary_source_url="https://www.courtlistener.com/docket/63107798/mata-v-avianca-inc/",
   jurisdiction="United States",language="en",ai_system_type="generative_text_llm",
   limen_categories="legal_procedural_contamination",
   paper_use_note="Court sanctioned counsel USD 5,000 (2023-06-22) for filing ChatGPT-fabricated citations and false statements.",
   verification_gap="Sanction is procedural; not a ruling on the underlying claim."),
 dict(case_id="LIMEN-WEB-004",record_status="state_ag_settlement",evidence_tier="T3_authoritative_source",
   title="Texas AG settlement with Pieces Technologies over overstated healthcare-AI accuracy",
   primary_source_id="Texas OAG press release + Assurance of Voluntary Compliance",primary_source_url="https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-reaches-settlement-first-its-kind-healthcare-generative-ai-investigation",
   jurisdiction="United States",language="en",ai_system_type="generative_clinical_summary_ai",
   limen_categories="ai_washing_or_false_ai_claim",
   paper_use_note="Texas AG (2024-09) resolved allegations that Pieces misrepresented its product's hallucination rate/accuracy; AVC imposes disclosure requirements (no monetary penalty).",
   verification_gap="Settlement (AVC) resolves allegations without admission; no court merits finding."),
 dict(case_id="LIMEN-WEB-005",record_status="regulator_decision_contested",evidence_tier="T2_contested_or_under_appeal",
   title="Garante (Italy) EUR 15M final fine on OpenAI over ChatGPT data processing",
   primary_source_id="Garante provvedimento 20 Dec 2024",primary_source_url="https://www.garanteprivacy.it/home/docweb/-/docweb-display/docweb/10085432",
   jurisdiction="Italy",language="it; en",ai_system_type="generative_text_llm",
   limen_categories="data_protection_enforcement",
   paper_use_note="Garante (2024-12-20) fined OpenAI EUR 15M for no legal basis, transparency and age-verification failures; ordered a 6-month awareness campaign.",
   verification_gap="OpenAI appealed; reporting indicates a Rome court subsequently set aside/curtailed the fine - cite as contested, not settled."),
 dict(case_id="LIMEN-WEB-006",record_status="court_ruling_then_settled",evidence_tier="T3_authoritative_source",
   title="Garcia v. Character Technologies: companion-chatbot product-liability suit over a teen's death",
   primary_source_id="M.D. Fla. 6:24-cv-01903, order 2025-05-21 (Conway J.)",primary_source_url="https://www.courtlistener.com/docket/69300919/garcia-v-character-technologies-inc/",
   jurisdiction="United States",language="en",ai_system_type="companion_chatbot",
   limen_categories="companion_chatbot_safety_harm",
   paper_use_note="Federal court (2025-05-21) denied dismissal in part, treating the chatbot as a product and rejecting a First-Amendment-speech defense; parties later settled (terms undisclosed).",
   verification_gap="Sensitive matter; cite only the docketed procedural rulings and the fact of settlement - no merits adjudication, no causal claim."),
 dict(case_id="LIMEN-WEB-007",record_status="court_certification",evidence_tier="T2_charging_or_procedural_stage",
   title="Mobley v. Workday: AI hiring-screening age-discrimination collective certified",
   primary_source_id="N.D. Cal. 3:23-cv-00770, order 2025-05-16 (Lin J.)",primary_source_url="https://clearinghouse.net/case/44074/",
   jurisdiction="United States",language="en",ai_system_type="ai_hiring_screening",
   limen_categories="education_workplace_or_hr",
   paper_use_note="Court (2025-05-16) granted preliminary ADEA collective certification, allowing a disparate-impact claim that Workday's AI screening discriminated by age to proceed.",
   verification_gap="Certification/procedural stage only; no liability finding on the merits."),
 dict(case_id="LIMEN-WEB-008",record_status="regulator_determination_under_review",evidence_tier="T2_contested_or_under_appeal",
   title="OAIC (Australia) determination: Bunnings facial recognition breached the Privacy Act",
   primary_source_id="OAIC determination 2024-11-19",primary_source_url="https://www.oaic.gov.au/news/media-centre/bunnings-breached-australians-privacy-with-facial-recognition-tool",
   jurisdiction="Australia",language="en",ai_system_type="facial_recognition",
   limen_categories="surveillance_biometrics_or_policing",
   paper_use_note="OAIC (2024-11-19) found Bunnings collected sensitive biometric data via in-store facial recognition without consent, breaching the Privacy Act.",
   verification_gap="Bunnings sought Administrative Review Tribunal review; determination is contested."),
 dict(case_id="LIMEN-WEB-009",record_status="regulator_preventive_then_lifted",evidence_tier="T2_authoritative_interim",
   title="ANPD (Brazil) preventive suspension of Meta's personal-data use for AI training",
   primary_source_id="ANPD preventive measure 2024-07-02",primary_source_url="https://www.gov.br/anpd/pt-br",
   jurisdiction="Brazil",language="pt; en",ai_system_type="generative_ai_training_pipeline",
   limen_categories="data_protection_enforcement",
   paper_use_note="ANPD (2024-07-02) ordered Meta to suspend using platform personal data for AI training (daily fine R$50k), citing legal-basis/transparency/minors concerns.",
   verification_gap="Preventive measure lifted 2024-08-30 after an approved compliance plan; interim, not a final penalty."),
 dict(case_id="LIMEN-WEB-010",record_status="regulator_final",evidence_tier="T3_authoritative_source",
   title="Garante (Italy) EUR 5M fine on Luka Inc. over the Replika companion chatbot",
   primary_source_id="EDPB national-news 2025 (Garante / Replika)",primary_source_url="https://www.edpb.europa.eu/news/national-news/2025/ai-italian-supervisory-authority-fines-company-behind-chatbot-replika_en",
   jurisdiction="Italy",language="it; en",ai_system_type="companion_chatbot",
   limen_categories="companion_chatbot_safety_harm;data_protection_enforcement",
   paper_use_note="Garante (2025) fined Luka Inc. EUR 5M for processing without a legal basis and lacking age verification on the Replika emotional-AI chatbot; opened a separate training-data probe.",
   verification_gap="Fine may be subject to appeal; separate generative-training probe ongoing."),
]
rows=[{**{h:"" for h in HEADER}, "access_date":AD, "impact_surface":"legal/regulatory", **r} for r in R]
with (ROOT/"results/security/limen-reviewed-core-web-verified-v0.1.tsv").open("w",encoding="utf-8",newline="") as fh:
    w=csv.DictWriter(fh,delimiter="\t",fieldnames=HEADER); w.writeheader(); w.writerows(rows)
print(f"web-verified reviewed-core records: {len(rows)}")
for r in rows: print(f"  {r['case_id']} [{r['evidence_tier'][:3]}] {r['jurisdiction'][:22]:22s} | {r['title'][:52]}")
