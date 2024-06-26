import json
from kafka import KafkaProducer

customer_points_data = {"customer_id": 1, "transaction_type":"EARN", "points": 5}

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    api_version='3.7.0',
)

producer.send(
    "customer_points_updates",
    json.dumps(customer_points_data).encode("utf-8"),
)
print("sent msg ", customer_points_data)

producer.flush()