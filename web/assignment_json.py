import urllib
import json

url = raw_input('Enter Url: ')
data = urllib.urlopen(url).read()
js = json.loads(str(data))

print sum(float(c['count']) for c in js['comments'])



