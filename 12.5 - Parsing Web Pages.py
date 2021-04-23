### Scrape legal olmayabilir.

### String aramalarını zor yoldan yapabilirsin ya da

### bedava uygulama olan Beautiful Soup'u www.crummy.com'dan indirebilirsin.


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()   #### .read() tek string
soup = BeautifulSoup(html, 'html.parser')

tags=  soup('a')        #### Retrieve all of the anchor tags.
for tag in tags:
    print(tag.get('href', None))
