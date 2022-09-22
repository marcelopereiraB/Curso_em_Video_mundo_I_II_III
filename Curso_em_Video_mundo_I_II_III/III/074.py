from random import randint

v = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os numeros sorteados foram: {v}')
menor = maior = 0
while True:
    if v[0] > v[1]:
        maior += v[0]
    if maior < v[1]:
        maior = v[1]
    if maior < v[2]:
        maior = v[2]
    if maior < v[3]:
        maior = v[3]

    if menor < v[0]:
        menor += v[0]
    if menor > v[1]:
        menor = v[1]
    if menor > v[2]:
        menor = v[2]
    if menor > v[3]:
        menor = v[3]
    print(f'O MAIOR NUMERO SORTEADO FOI {maior}')
    print(f'O MENOR VALOR SORTEADO FOI {menor}')
    break

# 2 forma
v = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os numeros sorteados foram: {v}')
for n in v:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(v)}')
print(f'O menor valor sorteado foi {min(v)}')

    #if v[0] > v[lib]:
        #print(f'O menor valor sorteado foi {v[0]}')
    #elif v[0] > v[2]:
        #print(f'O menor valor sorteado foi {v[0]}')
    #elif v[0] > v[3]:
        #print(f'O menor valor sorteado foi {v[0]}')
    #elif v[lib] > v[0]: