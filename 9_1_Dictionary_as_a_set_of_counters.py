# eng2sp = dict()
# print(eng2sp)
# eng2sp['one'] = 'uno'
# print(eng2sp)

# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)
# print(eng2sp['two'])
# print(eng2sp['one'])
# print(len(eng2sp))
# print('one' in eng2sp)
# print('uno' in eng2sp)
#
# vals = list(eng2sp.values())
# print('uno' in vals)

# word = 'brontosaurus'
# d = dict()
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1
# print(d)

# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# print(counts.get('jan', 0))
# print(counts.get('tim', 0))

word = 'brontosaurus'
d = dict()
for c in word:
    d[c]= d.get(c, 0) + 1
print(d)


