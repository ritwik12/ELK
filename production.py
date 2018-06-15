import timeit
start = timeit.default_timer()
id = set([])
views = ""
count = 0
lines = tuple(open("production.log", 'r'))
f =open("production.json","w") 
for i in range(1, len(lines)):
	line = lines[i]
	if line.find("Views")!=-1:
		id = line[20:28]
		count = count +1
		time = line[12:19]
	   	totaltime = line[line.find("in")+2: line.find("in")+7]
	   	Views = line[line.find("Views")+6: line.find("Views")+13]
	   	ActiveRecord = line[line.find("ActiveRecord")+14: line.find("ActiveRecord")+19]
		json = """{"index":{"_index":"production","_id":"""+'"'+str(i-1)+'"'+"""}} \n {"time":"""+'"'+time+'"'+""","Totaltime":"""+'"'+totaltime+'"'+""","ID ":"""+'"'+id+'"'+""","Views":"""+'"'+Views+'"'+""","ActiveRecord":"""+'"'+ActiveRecord+'"'+"}"
		print >>f, json