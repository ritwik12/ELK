import requests
import json
payload = open("irq.json")
url='http://localhost:9200/.kibana/visualization/IRQ2' #Visualization
#url='http://localhost:9200/.kibana/dashboard/Dash'    #Dashboard
r = requests.post(url, data=payload)
print(r.json())