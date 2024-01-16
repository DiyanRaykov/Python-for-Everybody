# def chop(t):
#     del t[0]
#     del t[-1]
#     # return None
#
# letters = ['a', 'b', 'c']
# print(chop(letters))
# print(letters)



def middle(t):
    return t[1:-1]

letters = ['a', 'b', 'c']
rest = middle(letters)
print(rest)
print(letters)
