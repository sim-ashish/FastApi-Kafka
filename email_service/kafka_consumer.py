from confluent_kafka import Consumer
import json
import threading

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'email-service-group',
    'auto.offset.reset': 'earliest'
})

def process_messages():
    consumer.subscribe(['user_created'])

    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("Consumer error:", msg.error())
            continue

        user = json.loads(msg.value().decode('utf-8'))
        print(f"📧 Sending welcome email to {user['email']}")

def start_consumer_thread():
    thread = threading.Thread(target=process_messages)
    thread.start()
