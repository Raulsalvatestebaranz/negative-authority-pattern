# Guardrails

This directory contains guardrails: contextual constraints derived from the Sociotechnical Constitution and applied within a specific scope.

Guardrails translate constitutional invariants into **locally binding** boundaries without redefining or overriding the constitution.

This README is not itself a guardrail. It defines what guardrails are allowed to be.

Guardrails that exist only in documentation, review artifacts, or stated intent — and not in lived system behavior — are considered violated.

---

## What guardrails are

Guardrails are constraints that exist to defend one or more governing invariants in a specific context.

They are allowed to say “never allowed” within their scope.

Guardrails may evolve as systems, tools, and contexts change.

---

## What guardrails are not

Guardrails are not:
- Universal law
- Interpretive guidance
- Best practices
- Decisions
- Operational instructions

If a constraint should apply everywhere, it does not belong here.

---

## Required properties of a guardrail

Every guardrail must explicitly state:

- **Scope** — where the guardrail applies and where it does not
- **Invariant protected** — which §4 invariant(s) it defends (at least §4.1 and/or §4.2)
- **Boundary** — what is never allowed within scope
- **Trade-off** — what flexibility or capability is reduced
- **Failure signals** — how humans can tell the guardrail is being violated

A guardrail that cannot state a boundary is not a guardrail.

---

## Authority boundary

Guardrails derive all authority from `CONSTITUTION.md`.

Guardrails may not:
- Introduce new invariants
- Override constitutional language
- Redefine constitutional terms
- Expand their scope implicitly

If a guardrail conflicts with the constitution, the guardrail is wrong.

---

## Change discipline

Guardrails may be added or modified when:
- Repeated failure occurs within a specific context
- The constitutional invariant at risk is clear
- The constraint is the minimal one that prevents recurrence

Guardrails should be removed when their scope no longer exists.

---

## Relationship to other documents

- `LEGITIMACY.md` defines whether a system is allowed to exist.
- `CONSTITUTION.md` defines what must never be violated.
- Guardrails define what is never allowed **locally**.
- Decisions record which guardrails were adopted.
- Exceptions record temporary violations of guardrails.

Guardrails do not decide outcomes or prescribe implementations.
