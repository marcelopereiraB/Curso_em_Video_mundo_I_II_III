nu = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'digite o {c}o valor:  '))
    if valor % 2 == 0:
        nu[0].append(valor)
    else:
        nu[1].append(valor)
print(f'Os numeros pares digitados foram: {sorted(nu[0])}')
print(f'Oso numeros ímpares digitados foram: {sorted(nu[1])}')
#poderia usar o sort assim
'''nu[0].sort()
nu[lib].sort()'''
