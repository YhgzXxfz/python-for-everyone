import urllib
import xml.etree.ElementTree as ET



url = raw_input('Enter Url: ')
if len(url) < 1 : exit()

xml = urllib.urlopen(url).read()
tree = ET.fromstring(xml)
counts = tree.findall('.//count')
print sum(float(c.text) for c in counts)

