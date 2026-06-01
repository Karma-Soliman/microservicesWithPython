## YOU NEED TO COMMIT THIS FILE BEFORE MOVING ON TO THE NEXT MODULE ! 🚨

**feel free to delete this comment**

# Module 1 — Reflection

**Team name**: **\*\***\_\_\_**\*\***
**Branch**: `module-01/<team-name>`
**Submitted**: before Module 2 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You started from a painful monolith. Now you're splitting it into separate services.

**What concrete problem does that split solve: and for whom?**

Think about it from three angles: the developer who has to change code, the team that has to deploy it, and the user who has to live with its failures. You don't need to cover all three, pick the one that felt most real to you today.

> _Your answer:_

The problem that felt most real today is the user one.

Splitting the monolith solves the problem of one change affecting the whole platform. It also helps failures stay smaller; if the notification-service crashes, users don't lose their feed or their ability to log games. In a monolith, the user has no platform at all.

---

## 2. Your choice

Look at your service map. Every arrow between two services is a decision someone made.

**Pick one boundary, one place where you decided service A should not be part of service B. Explain why that line exists.**

What would break, slow down, or become harder to manage if you merged those two services back together?

> _Your answer:_

I chose to keep activity-service separate from game-service. A game is catalogue data. An activity is user behavior. If these were merged, the game catalogue would become responsible for user behavior and feed logic, which would make it harder to evolve search, recommendations, and social features independently.

---

## 3. The tradeoff

Microservices solve the monolith's problems. But they create new ones.

**Name one thing that was simpler in the monolith and is now harder in your distributed design.**

No need to solve it: just name it honestly. This is exactly the tension the rest of the course is about.

> _Your answer:_

The monolith made function calls simple. Activity-service has to call game-service over HTTP and handle failure, partial failures to be exact.


---

_Keep this file. You will refer back to it during the oral presentation._
