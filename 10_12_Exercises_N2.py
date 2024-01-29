file_name = input('Enter a file name: ')  # mbox-short.txt
if len(file_name) < 1: file_name = 'mbox-short.txt'
try:
    fhand = open('mbox-short.txt')
except:
    print('The file name is not correct!', file_name)
    exit()

time = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    hour1 = words[5]
    hour2 = hour1.split(":")
    key = hour2[0]
    time[key] = time.get(key, 0) + 1

lst = []
for key, val in time.items():
    newtup = (key, val)
    lst.append(newtup)

lst = sorted(lst)
for key, val in lst:
    print(key, val)

