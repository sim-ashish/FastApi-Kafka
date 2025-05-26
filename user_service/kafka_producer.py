from confluent_kafka import Producer
import json

producer = Producer({'bootstrap.servers': 'localhost:9092'})

def send_user_created_event(user_data: dict):
    producer.produce('user_created', json.dumps(user_data).encode('utf-8'))
    producer.flush()
