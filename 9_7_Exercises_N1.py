ofile = open('words.txt')
text = dict()

for line in ofile:
    line.rstrip()
    if len(line) == 0: continue
    words = line.split()
    # print(words)

    for word in words:
        text[word] = text.get(word, 0) + 1
print(text)

print('from' in text)







