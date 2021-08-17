from kafka import KafkaConsumer
from AnalizeData.configs.config import ConfigKafka
from settings import KAFKA_LOCALHOST, GROUP_ID
import logging
import json


class KafkaConnection:
    def __init__(self):
        config = ConfigKafka()
        self.pages = config.parse_page()
        topics = config.parse_topics()
        if topics and self.pages:
            print("All is good")
            logging.info("Kafka data preparing")
            self.consumer = KafkaConsumer(topics["topic"], bootstrap_servers=KAFKA_LOCALHOST,
                                          auto_offset_reset='Early',
                                          enable_auto_commit=True, group_id=GROUP_ID, consumer_timeout_ms=1000,
                                          value_deserializer=lambda x: json.load(x.decode('utf-8')))
        else:
            raise Exception("File is not prepare")

    @classmethod
    def _make_json_data(cls, data: list):
        """
        NEED To make json for save in elasticsearch
        """
        return json.dumps(data)

    def get_data_consumer(self):
        for msg in self.consumer:
            # TODO передать данные
            print(msg)

    def start(self):
        pass
