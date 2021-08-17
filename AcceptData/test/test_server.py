from kafka import KafkaConsumer
from AnalizeData.configs.config import ConfigKafka
from settings import KAFKA_LOCALHOST, ROUTES
import requests


class ServerKafkaTest:
    @staticmethod
    def _visit_site_test(site):
        response = requests.get(ROUTES[site])
        if response.status_code is 200:
            print("Запрос отправлен")

    @staticmethod
    def _get_info_test():
        _topics = ConfigKafka.parse_topics()
        consumer = KafkaConsumer(_topics["topic"], bootstrap_servers=KAFKA_LOCALHOST)
        for msg in consumer:
            print(msg)


if __name__ == '__main__':
    pass
