#maneira 1
'''import math
n1 = int(input('digite um numero para fatorar: '))
while n1 > 0:
    fat = math.factorial(n1)
    print(f'o fatorial de {n1} é {fat}')
    break'''
#maneira 2
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
f = 1
while c > 0:
    print(f'{c}  ', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
