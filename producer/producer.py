from kafka import KafkaProducer
import json
import time

# Connect to Kafka broker
producer = KafkaProducer(
    bootstrap_servers="127.0.0.1:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    api_version=(2, 7, 0)
)

# Example student activity events
events = [
    {"student": "A", "action": "login"},
    {"student": "B", "action": "completed_quiz"},
    {"student": "A", "action": "logout"}
]

# Send events to Kafka
for event in events:
    producer.send("student_activity", event)
    print(f"Sent: {event}")
    time.sleep(1)  # wait 1 second between events

producer.flush()
