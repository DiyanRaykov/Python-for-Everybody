d = {'a':10, 'b':1, 'c':22}
l = list()
for key, val in list(d.items()):
    l.append((val, key))
    l.sort(reverse=True)
print(l)