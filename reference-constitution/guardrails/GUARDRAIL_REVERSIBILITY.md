# Guardrail: Reversibility

## Scope

This guardrail applies to any change that can materially affect users, operators, data, system behavior, or downstream systems once deployed.

This guardrail does not apply to changes that are strictly local, trivially undoable, or provably isolated from all meaningful impact.

---

## Invariant protected

This guardrail exists to protect:

- §4.2 Preserve human agency

---

## Boundary (never allowed)

Within this scope, the following is never allowed:

- Changes that cannot be safely rolled back, mitigated, or neutralized once applied.
- Changes whose failure modes permanently remove the ability for humans to intervene.
- Changes where recovery depends on heroics, manual data repair, or undocumented steps.
- Claimed reversibility that has not been exercised or validated under real operating conditions.

---

## Trade-off

This guardrail limits the speed and scope of change by requiring forethought about failure and recovery.

This trade-off is accepted to ensure humans retain the ability to act, recover, and regain control when changes behave unexpectedly or cause harm.

---

## Failure signals

This guardrail is likely being violated when:

- Rollback is described as “not possible” or “too risky.”
- Recovery plans exist only in theory or documentation.
- Failures require manual intervention under time pressure.
- Humans hesitate to intervene because stopping or undoing change would worsen the situation.
