from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")

doc_1 = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'email': 'taro@example.com',
    'timestamp': datetime.now(),
}
doc_2 = {
    'author': 'jack',
    'text': '今回は、全インデックスを一覧で取得したいので、引数のindexにはワイルドカードを指定します',
    'email': 'jack@example.com',
    'timestamp': datetime.now(),
}
doc_3 = {
    'author': 'tomy',
    'text': '接続しているElasticsearchでは、どのようなインデックスがあるのか確認したい場合は、cat属性のindices(index="*", h="index")を利用します。',
    'email': 'tomy@example.com',
    'timestamp': datetime.now(),
}

# Create indices
if es.indices.exists(index="students"):
    es.indices.delete(index="students")
else:
    es.indices.create(index='students')

# Insert docs
res = es.index(index="students", id=1, document=doc_1)
res = es.index(index="students", id=2, document=doc_2)
res = es.index(index="students", id=3, document=doc_3)

# Get doc
res = es.get(index="students", id=1)
print(res['_source'])
res = es.get(index="students", id=2)
print(res['_source'])
res = es.get(index="students", id=3)
print(res['_source'])

# Refreseh index
es.indices.refresh(index="students")

# Search:
# res = es.search(index="students", query={"match_all": {}})
res = es.search(index="students", query={"match": {"text": "ます"}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])