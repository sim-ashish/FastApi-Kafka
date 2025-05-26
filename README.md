# FastApi-Kafka
This Repository contains the basic demo to work with kafka and fastapi.
 - User Service – Registers users and sends user data to Kafka.

 - Email Service – Listens to Kafka for new user events and simulates sending welcome emails.

 - Kafka – Acts as the message broker.

---

## Requirements
 - **Python**
 - **Docker**
 - **fastapi**
 - **confluent-kafka**
 - **uvicorn**

## Running Commands

- Terminal 1
```bash
docker compose up
```

 - Terminal 2
 ```bash
 uvicorn user_service.main:app --reload --port 8000
 ```

  - Terminal 3 
```bash
uvicorn email_service.main:app --reload --port 8001
```