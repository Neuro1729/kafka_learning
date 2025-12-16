from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "student_activity",
    bootstrap_servers="127.0.0.1:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    api_version=(2, 7, 0)
)

print("Alert service listening...")

for message in consumer:
    if message.value.get("action") == "completed_quiz":
        print(f"ALERT: {message.value['student']} just completed a quiz!")
