min_num = None
max_num = None

while True:      # еквивалент на: password != 'Done':
    password = input('Enter a number: ')
    if password == 'done':
        break
    try:
        num = int(password)
    except:
        print('Invalid input')
        continue
    if min_num is None or min_num > num:
        min_num = num
    if max_num is None or max_num < num:
        max_num = num

print(f'Maximum is {max_num}')
print(f'Minimum is {min_num}')
