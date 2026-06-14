# Module 5 — Reflection

**Team name**: _______________
**Branch**: `module-05/<team-name>`
**Submitted**: before Module 6 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The game-service now has two models for the same data: SQLite for writes, Redis for reads. They store the same games in two different shapes.

**Why go through the trouble of maintaining two representations of the same data?**

Think about what kind of queries each model is optimised for, and what would happen if you tried to use the write model for high-traffic read operations.

> *Your answer:*

SQLite stores the full game record accurately and safely. Redis is a read model built for fast lookups of a smaller game summary. Maintaining both lets the system use the right tool for each job: SQLite for writes and correctness, Redis for high-traffic reads.

If every read hit the write model, traffic grows. So reading a small cached projection from Redis is faster and reduces pressure on SQLite.

---

## 2. Your choice

The logging-service checks GDPR consent before recording any activity. If a user has not opted in, the log is silently dropped.

**What does this consent check force you to accept about your data?** It is incomplete by design — some activities will never be recorded.

From a system design perspective: where is the right place to enforce this rule — in the logging-service, in the activity-service, or at the gateway? Why?

> *Your answer:*

The consent check forces us to accept that our logs are intentionally incomplete. If a user has not opted in, their activity may exist in activity-service, but logging-service must not store it.

I think the right place to enforce this is logging-service. It owns consent and log storage, so it should be the final authority on whether something is allowed to be recorded. If the gateway or activity-service made that decision, the rule could be bypassed by another producer later.

---

## 3. The tradeoff

With CQRS, your write model and read model can drift out of sync — a game is updated in SQLite but the Redis projection still shows the old data.

**In what scenario does this inconsistency matter to the user? In what scenario is it completely acceptable?**

Is there a class of applications where eventual consistency is never acceptable? What are they?

> *Your answer:*

The inconsistency matters if the stale Redis data changes what the user believes.

It is acceptable when the data is not critical and short-lived staleness does not harm the user. Eventual consistency is much less acceptable in systems like banking, payments, medical records, or legal consent state.

---

*Keep this file. You will refer back to it during the oral presentation.*
