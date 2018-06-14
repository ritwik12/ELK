file = open("production.log", "rt") 
contents = file.read()         
file.close()     
print contents.index("04:00:16")
print contents.index("04:00:24")   
start = contents.index("04:00:16") + 8 
end = contents.index("04:00:24")
str = contents[start:end] 
print str            
