from kafka import KafkaConsumer
from AnalizeData.configs.config import ConfigKafka
from settings import KAFKA_LOCALHOST
import logging
import subprocess


class KafkaConnection:
    def __init__(self):
        self.pages = ConfigKafka.parse_page()
        self.topics = ConfigKafka.parse_topics()
        if self.topics and self.pages:
            print("All is good")
            logging.info("Kafka data preparing")
            self.consumer = KafkaConsumer(self.topics["topic"], bootstrap_servers=KAFKA_LOCALHOST,
                                          auto_offset_reset='earliest',
                                          enable_auto_commit=False, consumer_timeout_ms=1000)
        else:
            raise Exception("File is not prepare")

    def get_data_consumer(self) -> dict:
        total = {}
        for msg in self.consumer:
            total.update(msg["value"].decode())

        self._clear_kafka_topic()
        return total

    def _clear_kafka_topic(self):
        subprocess.call(["/usr/bin/kafka-topics", "--zookeeper", "zookeeper-1:2181", "--delete", "--topic",
                         self.topics["topic"]])
