from AnalizeData.models.database import DataBase
from elasticsearch import Elasticsearch

INDEX_NAME = "aloha"

# Без вказування ID
# {'_index': 'aloha', '_type': '_doc', '_id': '1', '_score': 1.0, '_source':
# {'text': 'Elasticsearch31231231: cool. bonsai cool.'}}
# {'_index': 'aloha', '_type': '_doc', '_id': '2tB1ZHsBOI7NtlwanYLV', '_score': 1.0, '_source':
# {'text': 'Elasticsearch312331231231: cool. bonsai cool.'}}
# {'_index': 'aloha', '_type': '_doc', '_id': '2', '_score': 1.0, '_source':
# {'text': 'Elasticsearch312331231231: cool. bonsai cool.'}}


class DataBaseTest:
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if es.ping():
        print('Yay Connect')
    else:
        print('Awww it could not connect!')

    doc = {'text': 'cool. bonsai cool.'}
    #res = es.index(index=INDEX_NAME, id=2, body=doc)
    #print(res["result"])

    res = es.get(index=INDEX_NAME, id=2)
    print(res["_source"])
    es.indices.refresh(index=INDEX_NAME)

    res = es.search(index=INDEX_NAME, body={"query": {"match_all": {}}})
    print(res)
    for hit in res['hits']['hits']:
        print(hit)

    es.indices.delete(index=INDEX_NAME)

    res = es.search(index=INDEX_NAME, body={"query": {"match_all": {}}})
    print(res)


if __name__ == '__main__':
    DataBaseTest()

    base = DataBase()
    base.push_store({"site1": "localhost"})

