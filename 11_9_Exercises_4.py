import re # regex_sum_42.txt   regex_sum_1910800.txt

hand = open('regex_sum_42.txt')
numlist = list()
count = 0

for line in hand:
    line = line.rstrip()
    stuf = re.findall('([0-9]+)', line)
    if len(stuf) != 1: continue
    count += 1
    num = int(stuf[0])
    numlist.append(num)
print(count)
print(numlist)
total = int(sum(numlist))

print(total)