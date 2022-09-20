# metodos de adicionar em uma lista
lista = [1, 2, 3, 4, 5, 6]
lista2 = [10, 9, 6, 7, 4, 1, 2, 5]
lista.append(0)# final
nu = lista2.sort()
lista.insert(0, 'macaco') # add em qualquer lugar da lista com referencial do indice
# metodos de apagar elementos da lista
del lista[3]
lista.pop(3) #sem o indice/parametro ele apaga o ultimo elemento
lista.remove('macaco') # elimina o conteudo dentro do parametro
#criar lista
valor = list(range(1, 12))
print(sorted(lista2))# organiza
print(sorted(lista2, reverse=True)) #faz o inverso
print(lista)
print(valor)


lista3 = []
for cont in range(0, 5):
    lista3.append(int(input('digite um numero: ')))
for c, v in enumerate(lista3):
    print(f'no indice {c} esta armazenado o valor {v}')

a = [1, 2, 3, 4, 10]
b = [10, 9, 11, 12]
b = a # cria uma ligação entre as duas listas se eu mudar uma muda a outra

b[2] = 52
print(b)
print(a)
# fazendo copia de uma lista
b = a[:]# para todos os elementos de a agora estão dentro de b como uma copia
