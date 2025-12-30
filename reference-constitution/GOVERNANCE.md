# GOVERNANCE

## Purpose

This document defines how the Sociotechnical Constitution and its related documents are organized, interpreted, and changed over time. It exists to preserve clarity, prevent authority drift, and ensure that no document or process silently acquires power it is not permitted to hold.

This document does not define system behavior. If it conflicts with `CONSTITUTION.md` or `LEGITIMACY.md`, this document is wrong.

This document may not be used to justify deployment, continued operation, or enforcement decisions.

---

## Authority model

Authority flows strictly downward:

- `LEGITIMACY.md` defines whether a system is allowed to exist.
- `CONSTITUTION.md` defines what must never be violated once it exists.
- META–GOVERNANCE defines how documents relate and how authority is preserved.
- All other documents derive authority from the constitution and may not override it.

No document may reinterpret or weaken a higher-authority document.

**META–GOVERNANCE may not introduce new constraints, invariants, or prohibitions.**

---

## Document taxonomy

All documents in this repository must fall into exactly one of the following categories:

### Constitutional
Defines non-negotiable constraints that apply universally.
- Files: `LEGITIMACY.md`, `CONSTITUTION.md`
- Authority: absolute
- Change frequency: extremely rare

---

### Interpretive
Explains meaning without adding rules.
- Purpose: prevent misunderstanding
- May not introduce constraints
- May not override constitutional language

---

### Guardrails
Defines contextual constraints derived from the constitution.
- Authority: local only
- Must explicitly state which constitutional invariant they protect
- May evolve as context changes

---

### Decisions
Records durable choices and their trade-offs.
- Authority: historical only
- Decisions do not create rules
- Deprecated decisions are not rewritten

---

### Exceptions
Records explicit, temporary violations of constraints.
- Must name the violated invariant
- Must define scope, ownership, and sunset condition
- Undocumented exceptions are not permitted

---

### Operations
Supports humans in executing work.
- Authority: none
- Includes tools, checklists, workflows, and templates
- If operational artifacts conflict with any higher-level document, they must be ignored or removed

---

## Change control

Changes to constitutional documents are permitted only in response to repeated, observed failure in reality.

Any proposed change to `LEGITIMACY.md` or `CONSTITUTION.md` must:
- Identify the specific failure that necessitates the change
- Explain why existing language is insufficient
- Describe the minimal change required
- Explicitly state what the change does not allow

If these conditions cannot be met, the change must not be made.

---

## Anti-patterns (explicitly disallowed)

The following are not permitted:

- Multiple constitutions
- Domain-specific constitutions
- Rules hidden inside interpretive or operational documents
- Tools or processes that outrank human judgment
- “Best practices” presented as universal law
- Undocumented or permanent exceptions

---

## Interpretation rule

When ambiguity exists, documents must be interpreted in favor of preserving human understanding and human agency. Convenience, speed, performance, or preference must not be used to justify weakening constitutional constraints.

---

## Scope boundary

This document governs documentation structure and authority only. It does not govern system behavior, design decisions, or implementation details.

Those concerns belong to guardrails, decisions, and operations.
