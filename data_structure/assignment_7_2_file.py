# Use the file name mbox-short.txt as the file name
def extract_value(line):
    pos = line.find('.')
    return float(line[pos-1:])

fname = raw_input("Enter file name: ")
fh = open(fname)
total, count = 0,0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    total = total+extract_value(line)
    count = count+1
print "Average spam confidence:", float(total)/count

