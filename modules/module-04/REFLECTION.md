# Module 4 — Reflection

**Team name**: _______________
**Branch**: `module-04/<team-name>`
**Submitted**: before Module 5 lesson

---

Answer the three questions below. There are no right or wrong answers — we are looking for your reasoning, not a textbook definition. A few honest sentences are worth more than a long generic paragraph.

---

## 1. The "why"

In Module 3, services called each other directly over HTTP. Now activity-service drops a message into a broker and moves on — it never waits for a reply.

**What does the activity-service gain by not waiting? And what does the notification-service gain by consuming at its own pace?**

Think about what happens under load, or when notification-service is temporarily down.

> *Your answer:*

Activity-service gains speed. Once the activity is saved and the message is published to rabbitmq, the request can finish without depending on notification-service.

Notification-service gains the ability to move at its own pace. If notification-service is temporarily down, the activity request can still be sent through and the notifications can be processed later when it's up again.

---

## 2. Your choice

In Module 3 you already knew how to call another service directly over HTTP — you did it for user validation and game enrichment.

**Why not use the same approach for notifications? What does introducing a broker give you that a direct HTTP call doesn't?**

Think about what happens if notification-service is slow, or crashes mid-message.

> *Your answer:*

Notifications do not need to be part of the immediate activity response, so a direct HTTP call would be unnecessary. The broker allows us to decouple.

---

## 3. The tradeoff

With synchronous REST, you get an immediate answer: success or failure. With async messaging, the activity is saved and the message is sent — but you have no idea if the notification was ever delivered.

**How would a user know if their notification was never sent? How would you know as a developer?**

What visibility do you lose when you go async?

> *Your answer:*

They would only notice indirectly, for example if the notification does not appear in their notification list.

As a developer, I now need to observe RabbitMQ queues, consumer logs, database records. Going async makes the user request more resilient, but it also makes debugging harder because the work happens later and in another service.

---

*Keep this file. You will refer back to it during the oral presentation.*
