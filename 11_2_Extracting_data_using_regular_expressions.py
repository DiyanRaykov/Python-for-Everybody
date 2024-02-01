import re
hand = open('mbox-short.txt')
y = []
for line in hand:
    line = line.rstrip()
    # x = re.findall('\S+@\S+', line)
    x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', line)
    if len(x) > 0:
        y += x
        # print(x)
print(y)