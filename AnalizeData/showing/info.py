import logging
from datetime import datetime
from settings import LOG_DIR
import os


class ShowingInfo:
    @staticmethod
    def prepare_login():
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
