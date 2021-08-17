import os
import json
from settings import PATH_FILE_BASIC


class ConfigKafka:
    @staticmethod
    def parse_page() -> dict or None:
        """
            /data/site-page.txt read pages from file
        """
        path_file_pages = PATH_FILE_BASIC + "site-page.json"
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
        path_file_topics = PATH_FILE_BASIC + "topics.json"
        if not os.path.exists(path_file_topics):
            return None
        with open(path_file_topics, "r") as reader:
            data = json.load(reader)
        return data
