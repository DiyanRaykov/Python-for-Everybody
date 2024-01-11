# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[2])

fopen = open('mbox-short.txt')
for line in fopen:
    line = line.rstrip()
    if line.startswith('From '):
        list1 = line.split()
        print(list1[2])