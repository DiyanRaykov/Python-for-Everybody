file_name = input("Enter a file name: ")
try:
    fhand = open(file_name)
except:
    print('File cannot be opened:', file_name)
    exit()
f_open = open(file_name)
count = 0
total = 0
average = 0

for line in f_open:
    # line = ly.rstrip()
    if line.startswith("X-DSPAM-Confidence:"):
        begin = line.find(':')
        date = float(line[begin + 2:])
        count += 1
        total += date
        average = total / count

print('Average spam confidence:', average)
