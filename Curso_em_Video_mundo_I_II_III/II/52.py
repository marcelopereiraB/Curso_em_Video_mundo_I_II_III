import time
cont = 0
n = int(input('digite um numero: '))
print('Analisando...')
time.sleep(1)
if n > 1:
    for i in range(1, 11):
        if n % i == 0:
            cont += 1
    if cont > 2:
        print(f'não é primo, ele é divisivel {cont} vezes')
    else:
        print(f'é um numero primo, ele é disivivel apenas {cont}')
else:
    print('não é primo')
