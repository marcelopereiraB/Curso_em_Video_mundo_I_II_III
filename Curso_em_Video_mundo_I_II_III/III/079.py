numeros = list()
while True:
    n = int(input('digite um numero: '))
    if n not in numeros:
        numeros.append(n)
        print('valor adicionado com sucesso! ')
    else:
        print('valor duplicado! não inserido ')
    r = str(input('quer continuar? [S/N] '))
    if r in 'nN':
        print('obrigado')
        break
numeros.sort()
print(f'você digitou o valo {numeros}')
