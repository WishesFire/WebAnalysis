from elasticsearch import Elasticsearch, exceptions
from settings import HOST_NAME, HOST_ELASTIC, INDEX_NAME
from AnalizeData.controller.data import AcceptData
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

    @staticmethod
    def _save_file(data_elastic) -> None:
        with open("data_file.json", "w") as write_file:
            json.dump(data_elastic, write_file)

    def delete_store(self) -> None:
        try:
            self._connect_es.indices.delete(index=INDEX_NAME)
        except exceptions.NotFoundError:
            print("Index had already deleted")

    def get_all_store(self, search=None, save=False, only_all=False) -> dict:
        if search:
            res = self._connect_es.search(index=INDEX_NAME, body=search)
            return res
        else:
            res = self._connect_es.search(index=INDEX_NAME, body={"query": {"match_all": {}}})
            if save:
                self._save_file(res)
                self.delete_store()
            else:
                if only_all:
                    full_res = AcceptData(**res)
                    for elem in full_res:
                        print(elem)
                else:
                    for hit in res['hits']['hits']:
                        print(hit)
                return res
