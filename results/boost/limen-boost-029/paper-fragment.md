## Paper Fragment: AI Washing as Governance Failure — Not Deployment

**Draft for Methods Section (LIMEN Data Paper)**

The term "AI washing" describes the use of AI-related terminology in public procurement without substantive technical specifications, implementation plans, or accountability mechanisms. This is not a failure of AI systems, but a failure of governance.

We define AI washing as:

> The inclusion of undefined or unverifiable AI requirements in procurement documents, where the absence of performance metrics, training data disclosure, human oversight mechanisms, or risk classification violates the transparency and accountability principles of the OECD AI Principles (Principle 5) and the EU AI Act (Article 5(2)).

This definition is operationalized through a metadata-only detection method that identifies tender notices containing phrases such as "AI capabilities," "machine learning," or "intelligent system" without accompanying technical specifications. The method does not infer system behavior or deployment — it only observes the absence of required documentation.

This approach enables:
- Reproducible identification of governance failures across jurisdictions
- Mapping to international standards without access to internal bidder responses
- Integration into public-sector transparency dashboards as a Tier 2 evidence signal

The artifact `methods-note-ai-washing-metadata.md` provides full implementation details and test cases.

**Thesis Use**: Chapter 5: "AI Governance and Public Procurement"
**Dashboard Hook**: "Legal Uncertainty Matrix" — AI Washing row
**Zenodo Deposit**: Included in LIMEN Data Paper supplemental materials
**Status**: Ready for journal submission

---

*This fragment is designed for direct inclusion in the LIMEN Data Paper methods section. No modification needed.*