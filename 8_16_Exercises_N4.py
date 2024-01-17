all_words = list()
f_hand = open('romeo.txt')  # romeo.txt
for line in f_hand:
    words = line.split()
    all_words += words
    # print(all_words)
    if len(words) == 0:
        continue

new_list = []
for new in all_words:
    if new not in new_list:
        new_list.append(new)

sorted_word = new_list[:]
sorted_word.sort()
print(sorted_word)
