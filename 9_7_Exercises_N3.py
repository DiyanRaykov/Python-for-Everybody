file_name = input('Enter a file name: ')  # mbox-short.txt
try:
    fhand = open(file_name)
except:
    print('The file name is not correct!', file_name)
    exit()

e_mails = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) == 0: continue
    if words[0] != 'From': continue
    # print(words[2])
    sender = words[1]
    e_mails[sender] = e_mails.get(sender, 0) + 1

print(e_mails)