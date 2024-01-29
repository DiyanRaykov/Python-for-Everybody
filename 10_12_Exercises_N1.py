file_name = input('Enter a file name: ')  # mbox-short.txt
if len(file_name) < 1: file_name = 'mbox-short.txt'
try:
    fhand = open('mbox-short.txt')
except:
    print('The file name is not correct!', file_name)
    exit()

e_mails = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    key = words[1]
    e_mails[key] = e_mails.get(key, 0) + 1

lst = []
for key, val in e_mails.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:1]:
    print(key, val)

# горните два реда код могат да се изпълнят и така:
# a, b = lst[0]
# print(b, a)


# most = None
# for key, value in e_mails.items():
#     value = e_mails[key]
#     if most is None or value > most:
#         most = value
#         e_mail = key
# print(e_mail, most)
