# Exceptions

This document records explicit, temporary violations of the Sociotechnical Constitution or its derived guardrails.

Exceptions exist because reality exists. They are permitted only when their cost is acknowledged, bounded, owned, and time-limited.

This document does not grant permission. It records truth.

---

## What an exception is

An exception is a conscious decision to operate in violation of a constitutional invariant or guardrail for a limited time and scope.

An exception always represents accumulated failure.

---

## What an exception is not

An exception is not:
- A best practice
- A design pattern
- A default state
- A permanent configuration
- An undocumented workaround

Undocumented violations are not exceptions; they are failures.

---

## Required properties of an exception

Every exception must explicitly state:

- **Invariant or guardrail violated**
- **Scope** — what is affected and what is not
- **Owner** — a human accountable for the exception
- **Reason** — why this violation is necessary now
- **Mitigation** — how harm is limited while the exception exists
- **Sunset condition** — when or how the exception ends

An exception without a sunset condition is not permitted.

---

## Exception ledger

All active exceptions must appear in this ledger.

| ID | Violated invariant / guardrail | Scope | Owner | Reason | Sunset condition | Status |
|----|-------------------------------|-------|-------|--------|------------------|--------|
|    |                               |       |       |        |                  |        |

---

## Exception record template

Use the following template to record a new exception.

---

### Exception: <Short descriptive title>

- **ID:** EX-XXXX
- **Date recorded:** YYYY-MM-DD
- **Owner:** <Human owner>
- **Status:** Active | Closed

**Violated invariant or guardrail**  
(e.g. §4.2 Preserve human agency, GUARDRAIL_REVERSIBILITY)

**Scope**  
(What is affected. What is explicitly not affected.)

**Reason**  
(Why this violation is necessary now. Not “best practice”, not preference.)

**Mitigation**  
(How harm is limited while the exception exists.)

**Sunset condition**  
(Date, event, or state change that ends this exception.)

---

## Review discipline

Exceptions must be reviewed periodically.

If a sunset condition is missed, one of the following must occur:
- The exception is removed by doing the work
- The exception is re-recorded with a new owner and new sunset
- The violating system is shut down

Repeated exceptions of the same type constitute constitutional failure, not tolerance.

Exceptions that persist without review represent institutionalized failure.

---

## Relationship to other documents

- `LEGITIMACY.md` defines whether a system is allowed to exist.
- `CONSTITUTION.md` defines what must never be violated.
- Guardrails define what is never allowed locally.
- Exceptions record temporary truth when violations exist.

Exceptions do not redefine law. They record deviation from it.
