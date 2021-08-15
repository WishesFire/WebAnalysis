from kafka import KafkaProducer
from AnalizData.configs.config import ConfigKafka, KAFKA_LOCALHOST
import json

# Use a key for hashed-partitioning
producer = KafkaProducer(bootstrap_servers=KAFKA_LOCALHOST, value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('fizzbuzz', {'foo': 'bar'})