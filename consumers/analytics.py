from kafka import KafkaConsumer
import json
from collections import Counter

consumer = KafkaConsumer(
    "student_activity",
    bootstrap_servers="127.0.0.1:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    api_version=(2, 7, 0)
)

print("Analytics service listening...")

actions_counter = Counter()

for message in consumer:
    action = message.value.get("action")
    actions_counter[action] += 1
    print(f"Current stats: {dict(actions_counter)}")
