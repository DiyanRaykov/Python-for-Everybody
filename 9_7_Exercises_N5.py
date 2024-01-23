file_name = input('Enter a file name: ')  # mbox-short.txt
if len(file_name) < 1: file_name = 'mbox-short.txt'
try:
    fhand = open('mbox-short.txt')
except:
    print('The file name is not correct!', file_name)
    exit()

e_dom = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue

    key = words[1]
    begin = key.find('@')
    domain = (key[begin + 1:])
    e_dom[domain] = e_dom.get(domain, 0) + 1

print(e_dom)

# most = None
# for key, value in e_mails.items():
#     value = e_mails[key]
#     if most is None or value > most:
#         most = value
#         e_mail = key
# print(e_mail, most)
