import sys
import time
import logging
from .accept.activity import KafkaConnection
from AnalizeData.models.database import DataBase
from multiprocessing import Process
from AcceptData.server.main import run_server_forever
from .statistics.stat import Statistics
from .showing.info import ShowingInfo


def main():
    args = sys.argv
    ShowingInfo.prepare_login()
    logging.info("Start working!")

    if len(args) == 1:
        proc = Process(target=run_server_forever)
        proc.start()

        try:
            database = DataBase()
            logging.info("Prepare Database")

        except Exception as err:
            logging.error(f"Something happened - {err}")

        else:
            while True:
                try:
                    kafka = KafkaConnection()
                    data = kafka.get_data_consumer()
                    database.push_store(data)
                    time.sleep(60)

                except Exception as err:
                    logging.error(f"Something happened, try to make. Error - {err}")
                    time.sleep(20)

    elif len(args) > 1:
        stat = Statistics()
        stat.start()


if __name__ == "__main__":
    main()
