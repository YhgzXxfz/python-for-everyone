import re

fname = 'actual.txt'
handle = open(fname)
string = handle.read()
lst = re.findall('[0-9]+', string)

print sum(float(x) for x in lst)
