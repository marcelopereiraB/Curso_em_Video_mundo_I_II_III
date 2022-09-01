lista = list()
pares = list()
impares = list()
while True:
    nu = int(input('digite um numero: '))
    lista.append(nu)
    if nu % 2 == 0:
        pares.append(nu)
    else:
        impares.append(nu)
    r = str(input('quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        print('Obrigado')
        break
    while r not in 'SsNn':
        r = str(input(('dados invalidos, digite novamente: [S/N] ')))


print(f'a lista completa é {sorted(lista)}')
print(f'a lista de pares é {sorted(pares)}')
print(f'sua lista de impares é {sorted(impares)}')




