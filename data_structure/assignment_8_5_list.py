fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh :
    temp = line.split()
    if len(temp) < 1 : continue
    if temp[0] != 'From' : continue
        
    print temp[1]
    count = count + 1


    
print "There were", count, "lines in the file with From as the first word"

