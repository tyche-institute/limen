## Agentic‑Control Failure: Stored XSS in AI ChatBot Plugin

**Case ID:** CASE‑003

A public vulnerability (CVE‑2023‑4254) was reported for the *AI ChatBot* WordPress plugin (versions < 4.7.8). The flaw allows an administrator (or any high‑privilege user) to inject arbitrary JavaScript via the language‑settings page, which is stored and executed in the admin panel of any site using the plugin. While the vulnerability does not directly compromise the underlying LLM, it exemplifies how UI‑level injection can undermine agentic control by enabling malicious code execution in contexts that manage AI agents.

* **Evidence source:** https://cve.circl.lu/api/cve/CVE-2023-4254 (primary evidence tier).
* **Impact:** Enables an attacker to manipulate the bot’s configuration, potentially altering prompts or redirecting outputs without changing the model itself — a classic *agentic‑control failure*.
* **Relevance to LIMEN claims:** Supports the claim that *agentic control mechanisms can be subverted via web‑application vulnerabilities, even when the AI model itself is secure.*
* **Next steps:** Map this case to appropriate MITRE ATLAS and OWASP Agentic categories (e.g., `Injection → XSS`). Add mitigation notes (sanitize settings, enforce CSP).

*This fragment can be integrated into the “Security & Agentic Control” section of the upcoming LIMEN Edge‑Case Atlas manuscript.*