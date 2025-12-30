# CONSTITUTION

## 2) Prime law

> **A system is valid only as long as it preserves human understanding and human agency over time.**

If this becomes untrue, the system is constitutionally invalid; any continued operation is an explicit exception and will accumulate failure.

**Satisfaction of these invariants may not be demonstrated through documentation, process, review, or attestation alone.**

---

## 3) Terms (authoritative definitions)

The following terms are used with precise meaning throughout this constitution. If a system satisfies these terms only in theory, documentation, or intention—but not in lived operation—then the terms are not satisfied.

---

### Human understanding

Humans can form and maintain an accurate mental model of what the system is, what it does, why it behaves as it does, and how it can fail. Understanding exists only when competent humans can explain system behavior, predict outcomes within their area of responsibility, and recognize when the system is behaving incorrectly or unexpectedly.

Understanding is not satisfied by the existence of documentation, diagrams, or experts alone. If correct reasoning requires oral tradition, hero knowledge, or access to a specific individual, human understanding is not preserved.

---

### Human agency

Humans can meaningfully and safely influence the system over time. Agency exists only when humans can make changes, pause or stop behavior, undo or mitigate mistakes, recover from failure, and clearly exercise responsibility without requiring heroics or unsafe intervention.

Agency is not satisfied if control exists only in theory, only during normal operation, or only for a small subset of people. If safe change, recovery, or intervention depends on exceptional courage, luck, or undocumented procedures, human agency is not preserved.

---

### Preserve

To preserve a property means that it remains true as the system evolves in scale, complexity, ownership, and context. A property that holds only temporarily, only during initial design, or only under ideal conditions is not preserved.

---

### Over time

Over time includes system evolution, personnel change, incident conditions, partial failure, and sustained operation under real-world pressure. A system that preserves understanding or agency only during early development, normal operation, or under full staffing does not preserve them over time.

---

## 4) Governing invariants

This constitution is grounded in two non-negotiable invariants. A system that violates either invariant is already failing, regardless of intent, performance, or perceived necessity.

---

### 4.1 Preserve human understanding

#### Identity

Human understanding is preserved when humans can reliably comprehend the system as it exists and as it evolves.

#### Boundary (never allowed)

The following states are never allowed:

- Understanding that exists only in the mind of a single individual.
- Behavior that cannot be explained without tribal knowledge or oral tradition.
- Meaning hidden behind cleverness, magic, or implicit coupling.
- Systems whose observed behavior consistently diverges from how competent humans believe they work.

#### Meaning (what preservation looks like)

Human understanding is preserved when:

- Competent humans can build and maintain accurate mental models of the system.
- Humans can reason about change without requiring global knowledge.
- Surprise is rare, explainable, and bounded.

#### Failure signals

Human understanding is failing when:

- Onboarding relies more on conversation than on artifacts.
- Changes routinely require “ask the expert” to be safe.
- Debugging feels like archaeology rather than investigation.
- Humans cannot tell whether the system is behaving correctly without post-hoc explanation.

---

### 4.2 Preserve human agency

#### Identity

Human agency is preserved when humans can safely and meaningfully influence the system over time.

#### Boundary (never allowed)

The following states are never allowed:

- Change that requires heroics, courage, or ritual to perform safely.
- Failures that trap humans without a rollback or mitigation path.
- Ambiguous ownership during change or incident response.
- Safety that depends on individuals “being careful” rather than on structural properties.

#### Meaning (what preservation looks like)

Human agency is preserved when:

- Small changes are routine and low-risk.
- Mistakes can be undone or mitigated quickly.
- Responsibility and decision rights are clear at all times.

#### Failure signals

Human agency is failing when:

- Deployments are feared.
- Rollbacks are unreliable or impossible.
- Incidents are prolonged because fixes are risky.
- Work stalls due to unclear authority or ownership.
