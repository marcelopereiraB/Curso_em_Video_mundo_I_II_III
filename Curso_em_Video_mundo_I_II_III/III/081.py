lista = []

while True:
    nu = lista.append(int(input('digite um valor: ')))

    t = str(input('quer continuar? [N/S] ')).strip()[0]
    while t not in 'sSnN':
        t = str(input('dados invalidos. digite novamente [N/S] ')).strip()[0]
    if t in 'nN':
        print('Obrigado')
        break
lista.sort()
lista.reverse()
print(f'voce digitu {len(lista)} elementos')
print(f'os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'o numero 5 está na sua lista na posição {lista.index(5)}')
else:
    print('o numero 5 não esta na sua lista')
