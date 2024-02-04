import re # regex_sum_42.txt   regex_sum_1910800.txt

hand = open('regex_sum_1910800.txt')
numlist = list()
count = 0
total = 0

for line in hand:
    line = line.rstrip()
    nums_str = re.findall('[0-9]+', line)
    for n_str in nums_str:
        # count += 1
        num = int(n_str)
        numlist.append(num)
# print(count)
# print(numlist)
total = int(sum(numlist))
print(total)

