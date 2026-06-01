# Module 2 — Reflection

**Team name**: _______________
**Branch**: `module-02/<team-name>`
**Submitted**: before Module 3 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

You built a service with distinct layers: models, schemas, repository, service, and routes — each with a single responsibility.

**Why not just put everything in one file and call it done?**

Think about what happens six months later when someone new joins the team, or when you need to swap SQLite for PostgreSQL. What does the layered structure protect you from?

> *Your answer:*

The layered structure makes each file responsible for one kind of decision. And it makes the boundaries explicit, this protects us from mixing concerns so swapping SQLite for PostgreSQL means touching one file.


---

## 2. Your choice

Each service owns its data exclusively — no other service is allowed to touch its database directly.

**Pick one entity your service owns (e.g. `User`, `Game`). What would go wrong if another service could write to that table directly?**

Give a concrete scenario, not a general principle.

> *Your answer:*

I choose the `Game` entity.

If another service could write directly to the games table, it could create invalid or inconsistent catalogue data. For example, activity-service might insert a game while logging an activity, if it forgets required fields like genre or platform. Then the frontend search and game listing could show broken games. By forcing other services to go through the game-service API, the game-service keeps control over validation and the shape of game data.

---

## 3. The tradeoff

You now have models, schemas, a repository, a service, and routes — five layers for what is essentially a CRUD service.

**For a system this small, what is the cost of all this structure?**

And at what point does the complexity start to pay off? Where is the tipping point?

> *Your answer:*

 For only a few endpoints, the CRUD service now has many files. It feels slower than writing everything directly in `main.py`. There are also more imports and more setup work before the service runs.

The complexity starts to pay off when the service grows beyond simple CRUD: more endpoints, authentication, or multiple developers working at the same time. The tipping point is when changing one part of the service should not risk breaking the other part.

*Keep this file. You will refer back to it during the oral presentation.*
