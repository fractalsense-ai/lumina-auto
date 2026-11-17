# PLAN.md - Lumina Auto Vertical Baseline

_Last updated: 2026-11-15_

## Product and Repository Boundary

- `lumina-framework` remains the generic orchestration and governance engine.
- `lumina-biz` is the shared SMB business core.
- This public repository, `lumina-auto`, owns auto care, repair, and towing behavior.
- Customer-specific repositories are private and downstream of a supported vertical release.

Upstream baseline: `lumina-biz` commit `016dfae06fa9a1584eead1ebc6d7628d62472ed0`.

## Bootstrap Status

- The repository preserves the `lumina-biz` Git history and upstream lineage.
- The Python distribution is named `lumina-auto`; Python imports remain under `lumina` for compatibility with the inherited runtime.
- The initial `auto-repair` departmental pack now lives at the canonical `model-packs/auto-repair` path. Its legacy domain ID remains unchanged for compatibility.
- Shared connectors, routing, authentication, and orchestration remain inherited core surfaces. Do not copy or remove them without an explicit ownership decision.

## Runtime Boundaries

- Auto-owned behavior belongs in `lumina-auto`: auto service intake, diagnostics, estimates, repair/tow workflows, domain physics, and auto-specific adapters and fixtures.
- Reusable connectors, business identity hooks, task primitives, system-of-record guards, and audit behavior remain upstream in `lumina-biz` unless an explicit core change is accepted.
- Generic orchestration and governance belong in `lumina-framework`.
- Private customer repos may add customer-specific configuration and approved extensions; they must not contain credentials or production records.

## Next Work

1. Treat `lumina-auto` as the domain repo and `model-packs/auto-repair` as its first departmental model pack.
2. Keep the module ID `domain/bizops/auto-repair/v1` stable during the pack-path transition; any ID change requires a separate compatibility and data-migration decision.
3. Keep the existing API behavior available during migration; remove any core compatibility path only after vertical tests pass and a separate reviewed PR.
4. Add auto-care, repair, and towing acceptance scenarios before expanding or adding departmental packs.

## Verification and Delivery

- Every vertical change is a PR in `lumina-auto` and runs the vertical tests plus business-core compatibility checks.
- Record the base `lumina-biz` tag/commit for every upstream sync.
- Preserve system-of-record authority, Tool Token scope, human approval for mutations, and Slice 41's ERP execution gate.
- Keep manifests and hashes synchronized for documentation changes; never place customer secrets or production data in this public repository.
