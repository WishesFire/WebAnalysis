import os
import logging
import sys
from AnalizData.configs.config import LOG_DIR
from datetime import datetime


def main():
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
        pass

    elif len(args) > 1:
        pass


if __name__ == "__main__":
    main()
