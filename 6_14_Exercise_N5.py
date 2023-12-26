str = 'X-DSPAM-Confidence:0.8475'
begin = str.find(':')
final = len(str)
taken = str[begin+1:final+1]
str_to_float = float(taken)


# print(str.find(':'))
# print(final)
# print(taken)
# print(type(taken))
print(str_to_float)
# print(type(str_to_float))
