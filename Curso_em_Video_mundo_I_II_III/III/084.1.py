dados = list()
pessoas = list()
bebe = list()
bebe = ['bebe1', 19, 'bebe3', 'bebe4', 10]
dados.append('pedro')
dados.insert(1, 'gabriel')
dados.append(' marcelo')
pessoas.append(dados[:]) # copia considerando todos os elementos de uma lista na posição zero.
pessoas.append(bebe[:])
print(pessoas)
print(pessoas[1][1])
print(pessoas[0][1])
galera = [['marcelo', 21], ['alana', 16], ['karol', 38], ['marcio', 40]]
for p in galera:

    print(p)

gente = list()
gente2 = list()
for c in range(0, 3):
    gente2.append(str(input('nome: ')))
    gente2.append(int(input('idade: ')))
    gente.append(gente2[:])
    gente2.clear()
print(gente)
for y in gente:
    if y[1] > 18:
        print(f'{y[0]} é maior de idade')
    else:
        print(f'{y[0]} não é maior de idade')
