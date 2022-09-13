lista = []
for t in range(0, 5):
    lista.append(int(input('digite um numero: ')))
ma = lista.index(min(lista))
mi = lista.index(max(lista))
print(lista)

print(f'O maior valor digitado foi {max(lista)} na posição {mi}...')
print(f'O menor valor digitado foi {min(lista)} na posição {ma}...')
