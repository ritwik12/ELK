from elasticsearch import Elasticsearch

es = Elasticsearch()
#res = es.search(index="file1", body={"query": {"match": {"message": "a40e1704-325e-40f6-bde8-f107076e82b4"}}})
res = es.search(index="file1", body={"query": {"match": {"message": "a40e1704-325e-40f6-bde8-f107076e82b4"}}, "size" : 200})
print("%d documents found" % res['hits']['total'])
for doc in res['hits']['hits']:
    s = "%s" % ( doc['_source']['message']) # store data extracted from log file in a string
    str = s[0:29]+s[41:len(s)]
    print(str)
