import string

#  romeo-full.txt  romeo.txt mbox-short.txt mbox.txt
file_name = input('Enter a file name: ')
if len(file_name) < 1: file_name = 'mbox-short.txt'
try:
    fhand = open('mbox-short.txt')
except:
    print('The file name is not correct!', file_name)
    exit()
txt = ''
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', string.digits))
    line = line.lower()
    words = line.replace(" ", "")
    txt = txt + words.strip()

for index in range(len(txt)):
    counts[txt[index]] = counts.get(txt[index], 0) + 1

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)
for val, key in lst:
    print(key, val)
