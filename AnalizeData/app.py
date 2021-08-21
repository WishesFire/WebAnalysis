import os
import logging
import sys
import time
from settings import LOG_DIR
from datetime import datetime
from .accept.activity import KafkaConnection
from AnalizeData.models.database import DataBase
from multiprocessing import Process
from AcceptData.server.main import run_server_forever
from .statistics.stat import Statistics


def main():
    logging.info("Start working!")
    args = sys.argv
    report_time = str(datetime.now()).replace('-', '_').replace(':', '-')
    filename = report_time + '.log'
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    filepath = LOG_DIR + filename

    logging.basicConfig(
        filename=filepath,
        filemode='w',
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s'
    )

    if len(args) == 1:
        proc = Process(target=run_server_forever)
        proc.start()

    elif len(args) > 1:
        stat = Statistics()
        stat.start()

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


if __name__ == "__main__":
    main()
