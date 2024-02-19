# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
cnt = int(input('Enter count: '))
pos = int(input('Enter position: '))
# url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
print("Retrieving: ", url)
count = 0
for link in range(cnt):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    for tag in tags[:pos]:
        new_hrev = (tag.get('href', None))
    url = new_hrev
    print("Retrieving: ", url)
#
# Retrieve all of the anchor tags
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))