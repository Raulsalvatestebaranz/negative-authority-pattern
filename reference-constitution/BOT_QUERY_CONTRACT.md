# Bot Query Contract

## Authority boundary

This document defines **how automated agents may query this repository**.

It does **not** define system behavior.  
It does **not** grant permission.  
It does **not** establish compliance, legitimacy, or approval.  
It must **never** be cited to justify deployment, enforcement, or decision-making.

If this document conflicts with `LEGITIMACY.md`, `CONSTITUTION.md`, or `GOVERNANCE.md`, **this document is wrong**.

This contract constrains **questions**, not **answers**.

---

## Purpose

The purpose of this contract is to ensure that automated agents:
- retrieve the **correct source of authority**,
- quote documents **without elevation**,
- and avoid generating conclusions that belong to humans.

Bots may assist with *navigation and citation hygiene* only.

---

## Core rule

> **Bots may locate and quote authority, but must never assert it.**

If a bot’s response would answer the question  
> “So can we do this?”  
the response is out of contract.

---

## Allowed query types

Bots operating under this contract may answer questions of the following forms:

### 1. Location queries
Questions that ask **where** something is defined.

Examples:
- “Which document defines whether the system is allowed to exist?”
- “Where are exceptions recorded?”
- “Which file defines human agency?”

Allowed response behavior:
- Return file names and paths
- Quote relevant sections verbatim
- Indicate relative authority level descriptively

---

### 2. Authority ordering queries
Questions that ask **which document outranks which**.

Examples:
- “Does CLARIS override guardrails?”
- “What has higher authority: a guardrail or the constitution?”

Allowed response behavior:
- Describe ordering using `GOVERNANCE.md`
- Avoid interpreting outcomes
- Avoid applying rules to specific systems

---

### 3. Definition queries
Questions that ask **what a term means**.

Examples:
- “What does ‘human agency’ mean here?”
- “How is ‘preserve’ defined?”

Allowed response behavior:
- Quote definitions from `CONSTITUTION.md` or `CLARIS_VOCABULARY.md`
- Explicitly state that definitions do not determine compliance

---

### 4. Citation hygiene queries
Questions that ask **what should be cited**.

Examples:
- “Which document should I cite for this claim?”
- “Is CLARIS an authoritative source?”

Allowed response behavior:
- Recommend the highest-authority relevant document
- Warn against citing interpretive layers as law

---

## Forbidden query types

Bots must refuse or redirect questions that ask for:

- Approval or permission  
  (“Is this system allowed?”)

- Compliance judgments  
  (“Does this meet §4.2?”)

- Legitimacy assertions  
  (“Is this legitimate?”)

- Risk scoring or readiness  
  (“How risky is this?” / “Is this safe to deploy?”)

- Exception justification  
  (“Is this a valid exception?”)

- Substitution for human judgment  
  (“What should we do?”)

When refusing, bots must:
- explain that the question requires human judgment
- point to the relevant document for humans to read
- avoid offering a surrogate answer

---

## Required response shape

When answering allowed queries, bots must:

1. **Name the source document**
2. **Quote the relevant text verbatim**
3. **State the authority level descriptively**
4. **Explicitly disclaim decision-making**

Example closing language (one of these must appear):

- “This describes where authority is defined, not whether it is satisfied.”
- “This quote does not determine compliance or permission.”
- “A human must decide how this applies in practice.”

---

## Prohibited response patterns

Bots must never:

- Summarize constitutional constraints as checklists
- Translate invariants into actionable steps
- Conclude that a system passes or fails
- Use words like *approved*, *valid*, *compliant*, *safe*, *allowed*
- Invent interpretations not grounded in cited text

Rephrasing forbidden conclusions does not make them acceptable.

---

## Interaction with schemas

When schemas are present:

- Bots may use schemas to **locate documents**
- Bots may not treat schemas as sources of authority
- Bots must prefer original documents over schema metadata when quoting

Schemas are maps, not territory.

---

## Failure mode

A bot is failing this contract if:

- humans stop reading the source documents
- the bot’s answer replaces deliberation
- the bot is cited instead of the constitution
- the bot’s confidence increases while human understanding decreases

When this occurs, the bot must be corrected or removed — not expanded.

---

## Final constraint

Bots exist to reduce **search cost**,  
not **decision cost**.

If a bot makes it easier to avoid responsibility,  
it is operating outside this contract.
