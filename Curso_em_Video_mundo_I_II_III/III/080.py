lista = []
for m in range(0, 5):
    nu = int(input('digite um numero: '))
    if m == 0 or nu > lista[-1]:
        lista.append(nu)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if nu <= lista[pos]:
                lista.insert(pos, nu)
                print(f'adicionado na posição {pos}')
                break
            pos += 1
print(lista)
