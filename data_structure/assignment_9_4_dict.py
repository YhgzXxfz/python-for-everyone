name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()
for line in handle :
    temp = line.split()
    if len(temp) < 1 : continue
    
    if temp[0] == 'From' : 
        key = temp[1]
        dic[key] = dic.get(key, 0)+1
        
max_count, email = 0, ""
for key in dic :
    if dic[key] > max_count :
        max_count = dic[key]
        email = key

print email, max_count

