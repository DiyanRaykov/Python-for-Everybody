file_name = input('Enter a file name: ')  # mbox-short.txt
try:
    fhand = open(file_name)
except:
    print('The file name is not correct!', file_name)
    exit()
count = 0
for line in fhand:
    line = line.rstrip()
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0: continue
    if words[0] != 'From': continue
    count += 1

    print(words[1])
print(f'There were {count} lines in the file with From as the first word')