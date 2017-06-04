# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url = raw_input('Enter Url:  ')

count = int(raw_input('Enter Count: '))
pos = int(raw_input('Enter pos: '))

# Retrieve all of the anchor tags
for i in range(count) : 
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    c = 0
    for tag in tags :
        url = tag.get('href', None)
        c = c+1
        if c == pos : break


print url    
