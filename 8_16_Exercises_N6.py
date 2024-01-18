num = input('Enter a number: ')
num_list = []

while num != 'done':
    num = float(num)
    num_list.append(num)
    num = input('Enter a number: ')

print(f'Maximum: {max(num_list)}')
print(f'Minimum: {min(num_list)}')
