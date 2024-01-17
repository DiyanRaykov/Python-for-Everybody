file_name = input('Enter the file name: ') # mbox-short.txt
try:
    fhand = open(file_name)
except:
    print('The file name is not correct!', file_name)
    exit()

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From':
        continue

    print(words[2])


