from elasticsearch import Elasticsearch
from settings import HOST_NAME, HOST_ELASTIC, INDEX_NAME


class DataBase:
    def __init__(self):
        self._connect_es = self._create_elastic_object()

    @staticmethod
    def _create_elastic_object():
        connect_es = Elasticsearch([{"host": HOST_NAME, "port": HOST_ELASTIC}])
        if not connect_es.ping():
            raise Exception("Database is error")
        return connect_es

    def create_index(self):
        settings = {
            "settings": {
                "number_of_shards": 1,
                "number_of_replicas": 0
            },
            "mappings": {
                "pages": {
                    "dynamic": "strict",
                    "properties": {
                        "title": {
                            "type": "text"
                        },
                        "counts": {
                            "type": "integer"
                        }
                    }}}
                }
        try:
            if not self._connect_es.indices.exists(INDEX_NAME):
                self._connect_es.indices.create(index=INDEX_NAME, body=settings)

        except Exception as err:
            print(str(err))

    def push_store(self, record):
        outcome = self._connect_es.index(index=INDEX_NAME, doc_type="pages", body=record)
        print(outcome)
        if not outcome['result']:
            raise Exception("Something happened")

    def get_store(self, search):
        """
        {'query': {'match': {'calories': '102'}}}
        '_source': ['title'], 'query': {'range': {'calories': {'gte': 20}}}}
        json.dumps(search_object)
        """
        res = self._connect_es.search(index=INDEX_NAME, body=search)
        return res
