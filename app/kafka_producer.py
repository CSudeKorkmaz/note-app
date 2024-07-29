from kafka import KafkaProducer
import json

def get_kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer

def send_message(topic, message):
    producer = get_kafka_producer()
    producer.send(topic, message)
    producer.flush()
