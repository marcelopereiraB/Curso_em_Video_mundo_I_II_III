time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('nome da fera: '))
    tot = int(input('partidas jogadas: '))
    partidas.clear()
    for n in range(0, tot):
        partidas.append(int(input(f'quantos gols na partida {n+1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('quer continuar? [S/N] ')).upper()[0]
        if resp in 'SsNn':
            break
        print('erro! por favor digite S ou N.')
    if resp in 'N':
        break
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERROR! NÃO EXIXTE JOGADOR COM O CODIGO {busca}!')
    else:
        print(f'-- levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
        print('-'*40)
print('<< volte sempre >>')

