# Shared release bundle drift note v0.1

Generated: 2026-06-07T18:57:26Z
Lane: `limen-attestation-receipt-profile`
Project: `limen-ai-edge-case-atlas`
Target manifest: `results/attestation/shared-release-bundle-manifest-v0.1.tsv`

## Summary

- Recomputed live SHA-256 and byte counts for all 8 files named in the current shared release bundle manifest.
- Result: 2 members still match the manifest exactly; 6 member(s) have drifted or are missing.
- Drifted member IDs: attestation_profile, envelope_schema, attestation_status, dashboard_spec, article_architecture, preprint.
- Current trust posture remains `project_shared_local_bundle_only`.

## Why this matters

- The shared release bundle is a legitimate local publication object, but only for the exact file states captured when its manifest and `published` receipt were emitted.
- Later edits to bundle members do not invalidate the historical object, but they do make the manifest unsafe to cite as a live hash binding for changed files.
- This is a reviewer-useful negative result because it cleanly separates a valid historical local bundle snapshot from the current mutable working state.

## Conservative interpretation

- The manifest still supports bounded claims about one earlier local bundle snapshot.
- The manifest does not support a present-tense claim that all listed current files remain hash-identical to that earlier snapshot.
- No detached-signature, transparency-log, VC, truth, legality, compliance, certification, or safety witness is added by this audit.

## Suggested next safe move

- If Route C needs a current shared publication object, emit a refreshed manifest plus a new local `published` receipt over that refreshed manifest.
- Until then, cite the existing bundle as a historical local-release snapshot and pair it with `results/attestation/shared-release-bundle-drift-audit-v0.1.tsv` when discussing current live artifacts.
