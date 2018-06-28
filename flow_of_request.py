from elasticsearch import Elasticsearch
import re

es = Elasticsearch()
res = es.search(index="file1",scroll="10m", size="10000", body={"query": {"match_all": {}}})
sid = res['_scroll_id']
scroll_size = res['hits']['total']
count=0
ID= ""
print("%d documents found" % res['hits']['total'])
# Start scrolling
while (scroll_size > 0):
    res = es.scroll(scroll_id = sid, scroll = '10m')
    # Update the scroll ID
    sid = res['_scroll_id']
    # Get the number of results that we returned in the last scroll
    scroll_size = len(res['hits']['hits'])
    for doc in res['hits']['hits']:
        s = "%s)%s" % ( doc['_source']['source'],doc['_source']['message']) # store data extracted from    
        str = "%s" % ( doc['_source']['message'])
        m=re.search('[-a-zA-Z0-9]{36}', s) # regex to alphanumeric with hyphen 
        if m and s.find("production.log")!=-1:
            ID = s[m.start():m.end()]
        if s.find("candlepin.log")!=-1 and ID!="": # Fetch lines only from candlepin.log 
            if s.find(ID)!=-1:
                print("--------------------------------------------------------")
                print("Consumer id - "+ID)
                print(str)
                print("--------------------------------------------------------")