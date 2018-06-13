import re
import timeit
start = timeit.default_timer()
id = set([])
views = ""
count = 0
lines = tuple(open("production.log", 'r'))
#f =open("b.log","w") 
for i in range(1, len(lines)):
	line = lines[i]
	if line.find("Views")!=-1:
		id = line[20:28]
		count = count +1
		time = line[12:19]
	   	totaltime = line[line.find("in") + 2: line.find("in") + 8]
		print "Time", time
		print "Totaltime", totaltime
		print "ID", id
		print "-------------------------------------------------"	
	#	print >> f, time
	#	print >> f, totaltime
	#	print >> f, id
print count
print "Total IDs", count
stop = timeit.default_timer()
print "Run time:",stop - start 



                   