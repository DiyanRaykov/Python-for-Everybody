while True:
    line = input('> ')
    if len(line) > 0 and line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
