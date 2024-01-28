# list_of_ints_in_strings = ['42', '65', '12']
# list_of_ints = []
# for x in list_of_ints_in_strings:
#     list_of_ints.append(int(x))
#
# print(sum(list_of_ints))

#Същото като горното, но кратко:
list_of_ints_in_strings = ['42', '65', '12']
list_of_ints = [ int(x) for x in list_of_ints_in_strings ]
print(sum(list_of_ints))
