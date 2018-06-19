import os
#Create Index 
os.system("""curl -X PUT "localhost:9200/index" -H 'Content-Type: application/json' -d'
{
 "mappings": {
  "doc": {
   "properties": {
    "timestamp": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss"},
    "Totaltime": {"type": "float"},
    "ID": {"type": "keyword"},
    "Views": {"type": "float"},
    "ActiveRecord": {"type": "float"}
   }
  }
 }
}'
""")

#Add timestamp
os.system("""curl -X PUT "localhost:9200/_ingest/pipeline/timestamp" -H 'Content-Type: application/json' -d'  
{
  "description" : "Adds a timestamp field at the current time",
  "processors" : [ {
    "set" : {
      "field": "timestamp",
      "value": "{{_ingest.timestamp}}"
    }
  } ]
}
'
""")
#import data into index from json
os.system("curl -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9200/index/doc/_bulk?pretty' --data-binary @production.json")

