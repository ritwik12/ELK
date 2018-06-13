import re
count = 0
id = []
views = ""
with open("production1.log") as f:
    for line in f:
    	if re.match("^[A-Za-z0-9]*$", line[20:28]):
        	id.append(line[20:28])
id = list(set(id))
print "Total IDs", len(id)
with open("production1.log") as f:
	for line in f:
		for i in range(0,len(id)):
			if id[i] in line:
   				if line.find("Views")!=-1:
    					time = line[12:19]
    					totaltime = line[line.find("in") + 2: line.find("in") + 8 ]
    					ID = line[20:28]
    					print "Time", time
    					print "Totaltime", totaltime
    					print "ID", ID
    					print "-------------------------------------------------"	
    			

