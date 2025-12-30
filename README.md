
<!-- START FILE: NEGATIVE AUTHORITY PATTERN / README.md -->

# Negative Authority Pattern

## Authority boundary

This repository is **descriptive**. It does not govern any specific system.

This `README.md`:
- does **not** define system behavior
- does **not** grant permission to deploy or continue operating anything
- must **not** be cited to justify action, enforcement, or claims of compliance
- is wrong if it conflicts with anything inside `reference-constitution/`

If you’re looking for a rubber stamp, this repository only prints **“NO.”**

---

## What this is

A reusable governance pattern where authority is **purely subtractive**:

- legitimacy cannot be achieved, proven, or certified
- permission can only be **lost**, never granted
- interpretation can explain meaning but cannot decide outcomes
- machine-readable artifacts may help **locate** authority, but must never **exercise** it

This repository includes a **reference implementation** under `reference-constitution/`.

---

## What this is not

- not a policy suite
- not a compliance framework
- not an approval workflow
- not a checklist to “pass”
- not a tool for claiming legitimacy

Copying the reference files does not make anything legitimate. Reality does.

---

## Repository layout

```text
NEGATIVE AUTHORITY PATTERN
├── README.md
│   └── Pattern-level description (this file)
│
├── NEGATIVE_AUTHORITY_DOCTRINE.md
│   └── Meta-constraint on authority, certification, and misuse
│
├── OBSERVANCE_AND_CONSISTENCY.md
│   └── Explains how stability is preserved without review cycles or renewal
│
├── audits/
│   ├── TEMPLATE_AUDIT_ATTESTATION.md
│   └── AUDIT_ATTESTATION.md
│
└── reference-constitution/
    ├── LEGITIMACY.md
    │   └── Level −1: refusal / permission-to-exist
    ├── CONSTITUTION.md
    │   └── Level 0: governing invariants
    ├── GOVERNANCE.md
    │   └── META: authority structure / anti-drift
    ├── CLARIS.md
    │   └── Interpretive boundary
    ├── CLARIS_VOCABULARY.md
    ├── CLARIS_COMMON_MISUNDERSTANDINGS.md
    ├── CLARIS_CONFUSION_LOG.md
    ├── CLARIS_DRIFT_LOG.md
    ├── EXCEPTIONS.md
    ├── SCHEMA_RULES.md
    ├── BOT_QUERY_CONTRACT.md
    ├── constitution.index.schema.json
    ├── decisions/
    │   ├── ADR_TEMPLATE.md
    │   └── ADR-0001-Single-Constitution.md
    └── guardrails/
        ├── README.md
        ├── GUARDRAIL_TEMPLATE.md
        ├── GUARDRAIL_CLEAR_OWNERSHIP.md
        ├── GUARDRAIL_REVERSIBILITY.md
        └── GUARDRAIL_VISIBILITY.md
````

---

## How to use this repository (without breaking it)

* Use `reference-constitution/` as a **reference implementation** only.
* Create your own constitution inside the repository that owns the real system.
* Do not use this repository as a basis for approval, certification, or deployment gating.

In other words: **steal the shape, not the halo.**

---

## How consistency is preserved over time

This repository does **not** stay correct by being periodically reviewed, renewed, or re-approved.

It stays correct by:

* refusing certification
* avoiding artifact-based proof
* detecting misuse instead of chasing freshness
* changing **only** in response to demonstrated failure

There is **no expiration**, **no review cycle**, and **no update cadence**.

Details are documented in `OBSERVANCE_AND_CONSISTENCY.md`.

---

## Where authority lives (inside the reference)

1. `reference-constitution/LEGITIMACY.md`
2. `reference-constitution/CONSTITUTION.md`
3. `reference-constitution/GOVERNANCE.md`
4. Guardrails (scoped, local)
5. CLARIS (interpretive only)
6. Exceptions (explicit failure)
7. ADRs (history only)

This ordering is for navigation, not permission.

---

## Diagnostic assessment (non-authoritative)

This rating is **diagnostic only**.
It does **not** grant approval, permission, legitimacy, or readiness.

It reflects **misuse resistance and authority containment**, not correctness or safety.

**Score:** **9.5 / 10**

**Rationale:**

* The repository cannot be used to grant permission or legitimacy.
* Structural and social certification paths are explicitly blocked.
* Authority boundaries are visible and hard to invert.
* Remaining risk is social misuse under pressure, which cannot be eliminated by text alone.

<!-- END FILE: NEGATIVE AUTHORITY PATTERN / README.md -->


