word = """This program demonstrates another pattern of computation called a counter. The
variable count is initialized to 0 and then incremented each time an “a” is found.
When the loop exits, count contains the result: the total number of a’s."""
letter = ''

def counter(word1, letter1):
    count = 0
    for letter1 in word:
        if letter1 == 'a':
            count = count + 1
    return count

f = counter(word, letter)
print(f)