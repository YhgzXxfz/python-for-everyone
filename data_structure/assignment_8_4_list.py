fname = raw_input("Enter file name: ")
fh = open(fname)
st = set(fh.read().split())
lst = []
for word in st:
    lst.append(word)
lst.sort()
print(lst)

