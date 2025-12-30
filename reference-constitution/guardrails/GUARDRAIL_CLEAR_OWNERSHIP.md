# Guardrail: Clear Ownership

## Scope

This guardrail applies to any system, component, service, or automated capability that can affect users, operators, or downstream systems.

This guardrail does not apply to throwaway experiments that cannot affect others and can be safely discarded without consequence.

---

## Invariant protected

This guardrail exists to protect:

- §4.2 Preserve human agency

---

## Boundary (never allowed)

Within this scope, the following is never allowed:

- A system or component with no clearly identified human owner.
- Ambiguous or collective ownership where no individual or role has authority to decide, intervene, or accept responsibility.
- Situations where responsibility is deferred to a group, process, or the system itself.

---

## Trade-off

This guardrail reduces flexibility in how work is distributed and may slow decisions that rely on informal consensus.

This trade-off is accepted to preserve the ability for humans to act decisively, intervene safely, and remain accountable when the system changes or fails.

---

## Failure signals

This guardrail is likely being violated when:

- Incidents stall while ownership is debated.
- Changes are delayed because no one is authorized to decide.
- Responsibility shifts during failure (“it’s owned by everyone”).
- Humans hesitate to intervene due to unclear authority.
- Ownership exists only on paper, org charts, or escalation documents and cannot be exercised during incidents.

