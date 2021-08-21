from kafka import KafkaProducer, KafkaConsumer
from settings import KAFKA_LOCALHOST
import json


producer = KafkaProducer(bootstrap_servers=KAFKA_LOCALHOST,
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

producer.send("websites", {"localhost:8080": 1})


consumer = KafkaConsumer("websites", bootstrap_servers=KAFKA_LOCALHOST,
                         auto_offset_reset='earliest',
                         enable_auto_commit=False, consumer_timeout_ms=1000)
for msg in consumer:
    print(msg)
