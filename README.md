# **Student Activity Tracking System (Event-Driven)**

## **Project Overview**

This project demonstrates an **event-driven architecture** using **Apache Kafka, Docker, and Python**.
It tracks student activities in real time, such as login, quiz submissions, and logout, and processes them using multiple independent services.

**Key Idea:**
Instead of having services communicate directly, all events are sent to Kafka. Multiple consumers then process these events independently, enabling **scalable and decoupled systems**.

---

## **Architecture**

```
+----------------+       +------------------+       +-------------------+
|    Producer    |  -->  |      Kafka       |  -->  |    Consumers      |
|  (Python)      |       |  Broker Topic    |       |  Logger           |
| Sends student  |       |  student_activity|       |  Analytics        |
| activity events|       |                  |       |  Alerts           |
+----------------+       +------------------+       +-------------------+
```

**Components:**

1. **Producer**

   * Sends student activity events to Kafka.
   * Example events: `login`, `quiz submission`, `logout`.

2. **Kafka**

   * Central event backbone.
   * Stores messages in topics and allows multiple consumers to read independently.

3. **Consumers**

   * **Logger:** Logs all student events.
   * **Analytics:** Aggregates statistics (e.g., total logins, quizzes completed).
   * **Alert:** Sends alerts for specific actions (e.g., quiz completed).

---

## **Tech Stack**

* **Apache Kafka** – Event streaming platform
* **Zookeeper** – Kafka metadata and cluster management
* **Docker** – Containerization of Kafka, Zookeeper, and services
* **Python** – Producer and consumer services

---

## **Features**

* Real-time event tracking of student activities.
* Multiple independent consumers can process the same event.
* Fully containerized using Docker for easy setup and scalability.

---

## **Setup Instructions**

1. **Install Docker Desktop** with WSL 2 integration (Windows) or Docker (Linux/macOS).
2. **Clone the repository**:

```bash
git clone [<repo-url>](https://github.com/Neuro1729/kafka_learning.git)
cd kafka-learning
```

3. **Start Kafka and Zookeeper**:

```bash
sudo docker compose up -d
```

4. **Run consumers** (in separate terminals):

```bash
python3 consumers/logger.py
python3 consumers/analytics.py
python3 consumers/alert.py
```

5. **Run producer**:

```bash
python3 producer/producer.py
```

6. **Observe messages in real time** in consumer terminals.

---

## **Learning Outcomes**

* Hands-on experience with **Kafka topics, producers, and consumers**.
* Understanding **event-driven architecture** and **real-time processing**.
* Dockerized project demonstrates **scalable and portable deployment**.

---
