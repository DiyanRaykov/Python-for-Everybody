file_name = input('Enter the file name: ')
try:
    fhand = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', file_name)