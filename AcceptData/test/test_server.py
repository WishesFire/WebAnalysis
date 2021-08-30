from kafka import KafkaConsumer
from AnalizeData.configs.config import ConfigKafka
from settings import KAFKA_LOCALHOST, HOST_NAME, PORT_NUMBER
from AcceptData.server.main import run_server_forever
import threading
import requests
import platform
import socket
import subprocess


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


class ServerTest:
    def __init__(self, connection):
        if connection == "plain":
            socket.create_connection((HOST_NAME, PORT_NUMBER), timeout=10)
            self.success = True
        else:
            self.success = self._ping()

    @classmethod
    def _ping(cls) -> bool:
        try:
            output = subprocess.check_output("ping - {} 1 {}".format("n" if platform.system().lower() == "windows"
                                             else 'c', 'server'), shell=True, universal_newlines=True)
            if "unreachable" in output:
                return False
            else:
                return True
        except Exception:
            return False

    def get_result(self):
        return self.success


if __name__ == '__main__':
    th = threading.Thread(target=run_server_forever)
    th.start()

    ServerKafkaTest.visit_site_test()
    ServerKafkaTest.get_info_test()
