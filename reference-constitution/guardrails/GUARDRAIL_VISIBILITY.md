# Guardrail: Visibility / Observability

## Scope

This guardrail applies to any system, component, or automated capability whose behavior can materially affect users, operators, data, or downstream systems.

This guardrail does not apply to isolated, disposable experiments that cannot affect others and can be safely discarded without consequence.

---

## Invariant protected

This guardrail exists to protect:

- §4.1 Preserve human understanding
- §4.2 Preserve human agency

---

## Boundary (never allowed)

Within this scope, the following is never allowed:

- Systems whose critical behavior cannot be observed by responsible humans during normal operation and failure conditions.
- Failure modes that are detectable only after harm has scaled or after external reports.
- State changes or automated actions that cannot be traced back to an understandable cause within the system’s scope.
- Visibility that requires expert interpretation, post-hoc reconstruction, or external analysis to understand critical behavior.

---

## Trade-off

This guardrail increases implementation and operational overhead by requiring visibility into behavior, state, and failure.

This trade-off is accepted because humans cannot understand, intervene, or recover safely when system behavior is opaque.

---

## Failure signals

This guardrail is likely being violated when:

- Incidents are discovered via users, customers, or external systems rather than internal visibility.
- Humans cannot answer “what happened?” without reconstructing events manually.
- Debugging depends on guesswork or folklore rather than observable system behavior.
- Humans cannot tell whether the system is behaving correctly without post-hoc explanation.
