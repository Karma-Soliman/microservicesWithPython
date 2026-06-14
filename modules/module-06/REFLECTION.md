# Module 6 — Reflection

**Team name**: _______________
**Branch**: `module-06/<team-name>`
**Submitted**: before Module 7 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

The gateway now validates every JWT before forwarding a request. Individual services no longer need to check identity themselves.

**What does centralising authentication at the gateway buy you?** What would the alternative look like — if every service validated tokens on its own?

Think about what happens when you need to rotate the secret key, or add a new service to the system.

> *Your answer:*

Centralising authentication at the gateway gives the system one front door. The client sends a token once, the gateway verifies it, and invalid requests are rejected before reaching the services. This keeps the same identity check from being duplicated in every service.

If every service validated tokens independently, each service would need the same security logic, config, and secret management. Adding a new service would mean remembering to implement auth again. Rotating the secret key would also become harder because every service would need to be updated correctly.

---

## 2. Your choice

When activity-service calls user-service internally, it uses a Machine-to-Machine (M2M) token — not a user's token.

**Why can't it just reuse the user's token that arrived in the original request?**

What would break, or what door would you accidentally leave open, if services passed user tokens between themselves?

> *Your answer:*

It is activity-service performing a system-level validation. The M2M token makes that identity clear: the caller is the service, with role `service`.

If services passed user tokens around freely, user identity could leak deeper into the system than necessary. It would also make it harder to know whether an action was performed by the user or by a service on behalf of the workflow.
---

## 3. The tradeoff

The gateway and the auth-service share the same `SECRET_KEY` to verify tokens without making a network call on every request.

**What is the security risk of sharing this key?** What happens if it leaks?

And what would the alternative look like — verifying tokens by calling auth-service on every request instead? What does that cost you?

> *Your answer:*

Sharing the `SECRET_KEY` is powerful but risky. Any service with that key can verify tokens, but if the key leaks, an attacker could forge valid tokens and pretend to be any user or role, including admin.

The alternative is for the gateway to call auth-service on every request to verify the token. Hoever, it adds network latency and makes auth-service a critical dependency for every request. If auth-service is slow or down, the whole platform may become unavailable.

---

*Keep this file. You will refer back to it during the oral presentation.*
