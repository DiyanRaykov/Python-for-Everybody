import urllib.request, urllib.parse, urllib.error
import re

# url = input('Enter a URL address: ')  # url = 'http://data.pr4e.org/romeo-full.txt'
# if len(url) < 1: url = 'http://data.pr4e.org/romeo-full.txt'
url = 'http://data.pr4e.org/romeo-full.txt'

len_txt = 0
txt_all = ''

# Validate format URL
url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
if (not re.search(url_pattern, url)):
    print('The URL is not formatted!', url)
    exit()

# Validate open URL
try:
    fhand = urllib.request.urlopen(url)
except:
    print('The URL is not correct!', url)
    exit()

for line in fhand:
    str_line = line.decode() #.split()
    len_line = len(str_line)
    len_txt += len_line
    txt_all += str_line

print(txt_all[:3000])
print(len_txt)

# Validate exist URL
if line.decode().find('404 Not Found') == -1:
    print(line.decode(), end='')
else:
    print('The URL is not found!', url)
