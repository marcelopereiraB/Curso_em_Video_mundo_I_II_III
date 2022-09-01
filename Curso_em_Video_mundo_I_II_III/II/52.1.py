nu = int(input('ditige um numero: '))
tot = 0
for c in range(1, nu +1):
    if nu % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')

print(f'o numero {nu} foi divisivel {tot}')
if tot == 2:
    print('e por isso ele é primo')
else:
    print('e por isso ele não é primo')
