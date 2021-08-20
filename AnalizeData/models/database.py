from elasticsearch import Elasticsearch
from settings import HOST_NAME, HOST_ELASTIC, INDEX_NAME
import json


class DataBase:
    def __init__(self):
        self._connect_es = self._create_elastic_object()

    @staticmethod
    def _create_elastic_object() -> Elasticsearch:
        connect_es = Elasticsearch([{"host": HOST_NAME, "port": HOST_ELASTIC}])
        if not connect_es.ping():
            raise Exception("Database is error")
        return connect_es

    def push_store(self, doc: dict) -> None:
        outcome = self._connect_es.index(index=INDEX_NAME, doc_type="pages", body=doc)
        if not outcome['result']:
            raise Exception("Something happened")

    def get_all_store(self, search=None, save=False) -> None:
        # TODO save to json file
        if search:
            res = self._connect_es.search(index=INDEX_NAME, body=search)
            return res
        else:
            res = self._connect_es.search(index=INDEX_NAME, body={"query": {"match_all": {}}})
            if not save:
                for hit in res['hits']['hits']:
                    print(hit)
            else:
                with open("data_file.json", "w") as write_file:
                    json.dump(res, write_file)
