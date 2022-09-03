pessoas = dict()
lista = list()
lista_f = list()
cont = 0

while True:
    pessoas['nome'] = str(input('nome: '))
    pessoas['sexo'] = str(input('sexo: ')).strip()[0]
    pessoas['idade'] = int(input('idade: '))
    lista.append(pessoas.copy())
    lista_f.append(pessoas.copy())
    pessoas.clear()

    res = str(input('quer continuar? [S/N] ')).strip()[0]
    if res in 'Nn':
        break
for v, l in enumerate(lista_f):
    if lista_f[v]['sexo'] in 'mM':
        lista_f.pop(v)

for c in range(len(lista)):
    cont += lista[c]['idade']

media = cont / len(lista)
print('-=' * 30)
print(f'- Foram cadastradas {len(lista)} pessoas')
print(f'- A idade media do grupo {media:.2f} anos')
print('- As mulheres cadastradas foram: ', end=' ')
for b in range(len(lista_f)):
    print(f'{lista_f[b-1]["nome"]}, ', end='')
print()
for k, l in enumerate(lista):
    if lista[k]['idade'] > media:
        print('- istas das pessoas que estõ acima da média:')
        print(f' nome = {l["nome"]}; sexo = {l["sexo"]}; idade = {l["idade"]};')
        print()
print(lista_f)
print(lista)
print(v)
print(media)






