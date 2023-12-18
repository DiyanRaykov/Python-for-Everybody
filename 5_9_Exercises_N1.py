# password = ''
counter = 0
total = 0

while True:      # еквивалент на: password != 'Done':
    password = input('Enter a number: ')
    if password == 'done':
        break
    try:
        num = float(password)
    except:
        print('Invalid input')
        continue
    counter += 1
    total += num

avr = total / counter
print(total, counter, avr)
