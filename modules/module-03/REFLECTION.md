# Module 3 — Reflection

**Team name**: _______________
**Branch**: `module-03/<team-name>`
**Submitted**: before Module 4 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

All client requests now go through the gateway. No client ever calls a service directly.

**Why does that single entry point exist? What would the client's life look like without it?**

Think about what the client would need to know and manage if it talked to each service on its own port.

> *Your answer:*

The gateway gives the client one  entry point instead of making it know every service URL and port. Without it, the frontend would need to know that users are on port 8001, games are on 8002, and activities are on 8003. That would leak backend architecture into the client and make every service movement a frontend problem.

With the gateway, the client only talks to localhost:8000.


---

## 2. Your choice

The activity-service makes two outbound calls: one to validate the user (with retry logic), one to fetch game data (with a null fallback if it fails).

**Why are these two calls treated differently? Why does one retry and the other just give up gracefully?**

What is the consequence for the user in each case if the downstream service is unavailable?

> *Your answer:*

An activity should not exist for a user that does not exist. If user-service is temporarily unreachable, retrying once makes sense because the failure might be a network issue. If validation still fails, the activity should not be saved.

The activity can still be valid even if game-service is down. "game": null is better than failing the whole request. The user can still log the activity.


---

## 3. The tradeoff

Every time a client creates an activity, three services are involved synchronously. They all have to be running, healthy, and fast.

**What is the systemic risk of chaining synchronous calls like this?**

What happens to the user experience if the slowest service in the chain takes 3 seconds to respond?

> *Your answer:*


The risk of synchronous chaining is that the whole request becomes dependent on multiple services being available and fast. If one critical service is slow or unavailable, the user feels it immediately.

If the slowest service takes 3 seconds to respond, the whole request can take at least 3 seconds. That makes the app feel slow even if most services are healthy.

---

*Keep this file. You will refer back to it during the oral presentation.*
