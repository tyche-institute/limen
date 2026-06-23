# Detached-signature blocker note v0.1

Updated: 2026-06-08T21:17:54Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`
Status: blocker recorded; trust posture remains `project_shared_local_bundle_only`

## What was checked

- Confirmed the active shared signing target exists: `results/attestation/shared-release-bundle-manifest-v0.10.tsv` (`sha256:6eedcf774bad689baba01b534dc3fb065b0cd0b75382577eef9bf015c449b21e`). The older `v0.1` through `v0.9` manifests remain historical chronology only.
- Re-ran the local host tooling probe and verified that `openssl` and `gpg` are installed.
- Re-ran a bounded local `gpg --list-secret-keys` count probe without printing key material and observed `0` visible secret-key entries.
- Re-checked the project tree for detached-signature sidecars or public verification material (`*.sig`, `*.asc`, `*.pem`, `*.cer`, `*.crt`, `*.pub`). No attestation-specific signature or trust-anchor file was present; the only match was an unrelated bundled CA file inside `results/boost/limen-boost-009/tmp/ocr-venv/.../certifi/cacert.pem`.
- Re-read `results/attestation/detached-signature-verifier-experiment-request-v0.1.json` (`sha256:a94827d0d0718153e16af6085fd75c9d74d0e4c8cb8f9b10753ffcfa07f5cb54`), which now points the next witness attempt at the refreshed v0.10 bundle and still explicitly allows a fail-closed blocker outcome when safe signer provenance is unavailable.

## Negative result

This cycle did not produce a real detached-signature verifier note because no safe signer material or existing signature sidecar was visible under the lane's no-credential-exposure boundary. Tool availability alone is not enough to support any present-tense claim about signature verification, trust-anchor binding, external witnessing, or release integrity beyond the already documented local-bundle state.

## Claim impact

The attestation package still supports the bounded claim in `claims.md:LIMEN-C-014`: LIMEN can show machine-checkable observation-and-processing provenance plus one shared local publication bundle. It still does not show any detached-signature, transparency-log, VC-issuance, trust-anchor, truth, legality, compliance, certification, or safety witness.

## Paper/thesis/dashboard use

- Methods/limitations note: the next trust-surface upgrade is operationally specified but remains unavailable without safe signer material.
- Reviewer-response memo: the project chose a fail-closed blocker note instead of placeholder cryptographic theater.
- Dashboard provenance legend: keep signature/trust-anchor surfaces explicitly absent rather than visually implied.

## Next smallest safe move

Attempt a detached-signature verifier pass only if a later cycle receives pre-existing operator-managed signer material or an equivalent public verification artifact that can be referenced without printing or storing secrets in the repository. If that does not become available, keep the route blocked and do not widen placeholder fields.
