# file_name = input('Enter a file name: ')   #  romeo-full.txt  romeo.txt mbox-short.txt mbox.txt
# if len(file_name) < 1: file_name = 'mbox.txt'
# try:
#     fhand = open('mbox.txt')
# except:
#     print('The file name is not correct!', file_name)
#     exit()

import re

hand = open('mbox.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuf = re.findall('New Revision: ([0-9]+)', line)
    if len(stuf) != 1: continue
    num = int(stuf[0])
    numlist.append(num)
ave = int(sum(numlist) / len(numlist))

print(ave)
