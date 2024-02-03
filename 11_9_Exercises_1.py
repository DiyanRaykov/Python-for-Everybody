import re

# file_name = input('Enter a file name: ')   #  romeo-full.txt  romeo.txt mbox-short.txt mbox.txt
# if len(file_name) < 1: file_name = 'mbox.txt'
# try:
#     fhand = open('mbox.txt')
# except:
#     print('The file name is not correct!', file_name)
#     exit()

fhand = open('mbox.txt')
reg = input('Enter a regular expression: ') # ^From:.+@, ^Author
count = 0

for line in fhand:
    line = line.rstrip()
    if re.search(reg, line):
        count += 1
print(count)
