import os
import json
from dotenv import load_dotenv

load_dotenv()
LOG_DIR = "logs/"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INDEX_NAME = "web-analysis"
PATH_FILE_BASIC = BASE_DIR + "\\data\\"

KAFKA_LOCALHOST = "localhost:9092"
GROUP_ID = "counters"


class ConfigKafka:
    @staticmethod
    def parse_page() -> dict or None:
        """
            /data/site-page.txt read pages from file
        """
        path_file_pages = PATH_FILE_BASIC + "site-page.txt"
        if not os.path.exists(path_file_pages):
            return None
        with open(path_file_pages, "r") as reader:
            data = json.load(reader)
        return data

    @staticmethod
    def parse_topics() -> dict or None:
        """
            /data/topics.txt read topics from file
        """
        path_file_topics = PATH_FILE_BASIC + "topics.txt"
        if not os.path.exists(path_file_topics):
            return None
        with open(path_file_topics, "r") as reader:
            data = json.load(reader)
        return data
