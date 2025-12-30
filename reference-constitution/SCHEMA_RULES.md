# Schema Rules

## Authority boundary

This document governs **machine-readable schemas only**.

It does **not** define system behavior.  
It does **not** grant permission.  
It does **not** determine legitimacy, compliance, approval, readiness, or safety.  
It must **never** be cited to justify deployment, continued operation, enforcement, gating, or claims of correctness.

If this document conflicts with `LEGITIMACY.md`, `CONSTITUTION.md`, or `GOVERNANCE.md`, **this document is wrong**.

This document constrains *schemas*, not reality.

---

## Purpose

The purpose of these rules is to ensure that machine-readable artifacts:

- help humans and machines **locate** the correct documents,
- improve **navigation, retrieval, and citation hygiene**,
- without allowing machines to **decide**, **judge**, **score**, or **certify** anything.

Schemas exist to reduce confusion — not to transfer authority.

---

## Core principle

> **A schema may describe where authority lives, but must never exercise it.**

Any schema that enables conclusions about legitimacy, compliance, permission, approval, readiness, confidence, or satisfaction violates this principle.

---

## Anti-certification boundary

No schema, index, or machine-readable artifact in this repository may be used to certify, approve, validate, or attest to the legitimacy, correctness, safety, or compliance of any system.

These artifacts are descriptive only. They exist to locate and reference authority, not to exercise it.

Any use of schema output as evidence of approval, readiness, or acceptability constitutes misuse of this repository.

---

## What schemas are allowed to do

Schemas in this repository may:

- Index documents and their repository-relative paths
- Classify documents by type (e.g. constitution, guardrail, interpretive)
- Describe relative authority levels **for navigation and citation hygiene only**
- Provide human-readable metadata (titles, summaries, scope, tags, ownership)
- Reference constitutional invariants **by identifier only**
- Support search, navigation, and citation hygiene
- Fail validation when unexpected or unsafe fields are introduced

Schemas exist to help machines **find the right document**, not to replace reading it.

---

## What schemas are never allowed to do

Schemas must never:

- Express compliance or non-compliance
- Express legitimacy or illegitimacy
- Express approval, certification, authorization, or readiness
- Express “pass”, “fail”, “status”, or “risk”
- Encode decision logic, thresholds, or evaluations
- Encode conditions under which action is allowed or blocked
- Replace or shortcut human judgment

If a field answers the question:

> “So can we do this?”

…it does not belong in a schema.

---

## Forbidden field patterns

The following concepts must never appear in any schema — explicitly or implicitly:

- `approved`
- `valid`
- `legitimate`
- `compliant`
- `meets`
- `satisfies`
- `status`
- `ready`
- `allowed`
- `blocked`
- `risk`
- `riskLevel`
- `confidence`
- `score`
- boolean flags that imply evaluation rather than description

Renaming these concepts does not make them acceptable.

---

## Required defensive properties

Every schema must include, wherever feasible:

1. **Explicit non-authority signaling**  
   Clear language stating the schema has no authority and cannot justify action.

2. **No silent extension**  
   `additionalProperties: false` must be used to prevent accidental power creep.

3. **Descriptive, not evaluative language**  
   Enums and fields must describe *type*, *category*, or *location* — never fitness.

4. **Human-readable ambiguity where risk exists**  
   When interpretation could imply judgment, prefer free-text fields over machine-actionable ones.

---

## Schema evolution rules

Schemas may evolve only to:

- Add new document classifications
- Add new **navigational or informational metadata**
- Improve clarity for indexing, retrieval, or citation hygiene
- Strengthen defenses against misuse or authority creep

Schemas may **not** evolve to:

- Answer new decision questions
- Automate review, gating, or enforcement
- Encode constitutional reasoning
- Make bots more confident about acting
- Replace humans reading source documents

If a proposed schema change would reduce human deliberation, the change is not allowed.

---

## Relationship to the Constitution

Schemas are subordinate to all constitutional documents.

In order of authority:

1. `LEGITIMACY.md`
2. `CONSTITUTION.md`
3. `GOVERNANCE.md`
4. Guardrails (within scope)
5. Schemas (navigation only)

Schemas may never outrank, reinterpret, operationalize, or summarize constitutional text as rules.

---

## Failure mode

A schema is failing when:

- It is cited as evidence of compliance or legitimacy
- It is used to justify action or inaction
- It becomes a substitute for reading the source documents
- Humans stop arguing because “the schema says so”
- Bots are trusted more than the constitution itself

When this occurs, the schema must be corrected or removed — not expanded.

---

## Final constraint

Schemas exist to help machines **ask better questions**,  
not to let them **answer the wrong ones**.

If a schema makes it easier to avoid human responsibility,  
it has already failed.
