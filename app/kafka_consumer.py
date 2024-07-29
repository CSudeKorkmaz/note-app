from kafka import KafkaConsumer
import json

def get_kafka_consumer(topic):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='kafka:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    return consumer

def consume_messages(topic):
    consumer = get_kafka_consumer(topic)
    for message in consumer:
        print(message.value)
