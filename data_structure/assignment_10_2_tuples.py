name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

dic = dict()

for line in handle :
    temp = line.split()
    if len(temp) < 1 : continue
    if temp[0] != 'From' : continue
    hour = temp[5].split(':')[0]
    dic[hour] = dic.get(hour, 0)+1



for k in sorted(dic) :
    print k,dic[k]
