import re
import timeit
start = timeit.default_timer()
id = set([])
views = ""
count = 0
lines = tuple(open("production.log", 'r'))
#f =open("output.log","w") 
for i in range(1, len(lines)):
	line = lines[i]
	if line.find("Views")!=-1:
		id = line[20:28]
		count = count +1
		time = line[12:19]
	   	totaltime = line[line.find("in")+2: line.find("in")+7]
	   	Views = line[line.find("Views")+6: line.find("Views")+13]
	   	ActiveRecord = line[line.find("ActiveRecord")+14: line.find("ActiveRecord")+19]
		print "Time :", time
		print "Totaltime :", totaltime
		print "ID :", id
		print "Views :", Views
		print "ActiveRecord :", ActiveRecord
		print "-------------------------------------------------"	
	#   Print to File
	#	print >> f, time
	#	print >> f, totaltime
	#	print >> f, id
print count
print "Total IDs", count
stop = timeit.default_timer()
print "Run time:",stop - start 



                   