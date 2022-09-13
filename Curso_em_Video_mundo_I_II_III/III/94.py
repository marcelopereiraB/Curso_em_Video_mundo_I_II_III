pessoas = dict()
lista = list()
cont = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('nome: '))
    pessoas['sexo'] = str(input('sexo: [M/F] ')).strip()[0]
    while pessoas['sexo'] not in 'MmFf':
        print('ERRO! por favor digite, apenas F ou M.')
        pessoas['sexo'] = str(input('sexo: [M/F] ')).strip()[0]
    pessoas['idade'] = int(input('idade: '))
    lista.append(pessoas.copy())
    while True:
        res = str(input('quer continuar? [S/N] ')).strip()[0]
        if res not in 'sSnN':
            print('ERRO! por favor digite, apenas F ou M.')
        if res in 'sSnN':
            break
    if res in 'Nn':
        break
for c in range(len(lista)):
    cont += lista[c]['idade']

media = cont / len(lista)
print('-=' * 30)
print(f'- Ao todo foram cadastradas {len(lista)} pessoas')
print(f'- A idade media do grupo {media:.2f} anos')
print('- As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end='. ')
print()
print('- listas das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] > media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()

#curso em video
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('nome: '))
    while True:
        pessoa['sexo'] = str(input('sexo: [S/M] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N.')
    if resp == 'N':
        break

print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A media de idade é de {média:5.2f} anos')
print(f'As mulheres cadastradas foram', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(' listas das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= média:
        print('      ')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')

