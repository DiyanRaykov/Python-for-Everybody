import socket
import re

url = input('Enter a URL address: ')    # http://data.pr4e.org/romeo.txt
if len(url) < 1: url = 'http://data.pr4e.org/romeo.txt'
url1 = url.split('/')
host = url1[2]

# Validate format URL
url_pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
if (not re.search(url_pattern, url)):
    print('The URL is not formatted!', url)
    exit()

# Validate open URL
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
except:
    print('The URL is not correct!', url)
    exit()

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # Validate exist URL
    if data.decode().find('404 Not Found') == -1:
        print(data.decode(), end='')
    else:
        print('The URL is not found!', url)

mysock.close()
