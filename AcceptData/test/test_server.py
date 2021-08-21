from kafka import KafkaConsumer
from AnalizeData.configs.config import ConfigKafka
from settings import KAFKA_LOCALHOST
from AcceptData.server.main import run_server_forever
import threading
import requests


class ServerKafkaTest:
    @staticmethod
    def visit_site_test() -> None:
        response = requests.get("http://localhost:8000/")
        if response.status_code is 200:
            print("Запрос отправлен")

    @staticmethod
    def get_info_test() -> None:
        _topics = ConfigKafka.parse_topics()
        consumer = KafkaConsumer(_topics["topic"], bootstrap_servers=KAFKA_LOCALHOST,
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=False, consumer_timeout_ms=1000)
        for msg in consumer:
            print(msg)


if __name__ == '__main__':
    th = threading.Thread(target=run_server_forever)
    th.start()

    ServerKafkaTest.visit_site_test()
    ServerKafkaTest.get_info_test()
