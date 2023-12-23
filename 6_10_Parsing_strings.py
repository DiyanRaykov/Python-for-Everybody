
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
begin = data.find('@')
print(begin)

final = data.find(' ', begin)
print(final)

host = data[begin + 1:final]
print(host)
