pessoas = dict()
lista = list()
lista_feminina = list()
cont = 0
cont1 = 0
while True:
    pessoas['nome'] = str(input('nome: '))
    pessoas['sexo'] = str(input('sexo: ')).strip()[0]
    pessoas['idade'] = int(input('idade: '))
    lista.append(pessoas.copy())
    pessoas.clear()

    res = str(input('quer continuar? [S/N] ')).strip()[0]
    if res in 'Nn':
        break
print(f'foram cadastradas {len(lista)}')
for l, n in enumerate(lista):
    if lista[0]['sexo'] in 'Ff':
        lista_feminina.append(pessoas.copy())
print(f'{l} {n}')
print(lista_feminina)
