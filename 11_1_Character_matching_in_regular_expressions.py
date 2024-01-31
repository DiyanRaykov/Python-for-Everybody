# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if re.search('^F..m:', line):
#         print(line)

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)