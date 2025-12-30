# Architecture Decision Record

## ID
ADR-0001

## Title
Single Sociotechnical Constitution

## Date
YYYY-MM-DD

## Status
Accepted

This record is historical. It does not create rules, grant permission, or justify enforcement.

---

## Context

As the system evolved, authority and constraints became distributed across multiple documents, operating systems, and agreements. This created ambiguity about which rules were fundamental, which were contextual, and which were historical.

This ambiguity made it difficult to reason about legitimacy, responsibility, and long-term system behavior, and increased the risk of silent authority drift.

---

## Decision

We adopt exactly one Sociotechnical Constitution as the single source of non-negotiable system-wide constraints.

All other documents derive authority from this constitution and may not override or reinterpret it.

---

## Rationale

A single constitution prevents self-competition between rules, reduces ambiguity during failure, and makes authority explicit and inspectable.

This decision aligns with the constitutional invariants of preserving human understanding and preserving human agency by ensuring that humans always know which constraints apply and where responsibility lies.

---

## Consequences

Positive consequences:
- Clear authority hierarchy
- Reduced interpretive drift
- Explicit handling of exceptions

Negative consequences:
- Reduced flexibility in introducing system-wide rules
- Increased friction for changes to foundational constraints

---

## Alternatives considered

- Multiple domain-specific constitutions  
  Rejected because it reintroduces ambiguity and competing authority.

- Implicit constitutional norms  
  Rejected because they drift silently over time.

---

## Reversibility

This decision can be reversed only by adopting a new constitution and explicitly deprecating the existing one.

Such a reversal would be costly and disruptive by design.
