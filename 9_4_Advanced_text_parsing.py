# import string
# print(string.punctuation)

import string

fname = input('Enter the file name: ') # romeo-full.txt
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        # if word not in counts:
        #     counts[word] = 1
        # else:
        #     counts[word] += 1
print(counts)