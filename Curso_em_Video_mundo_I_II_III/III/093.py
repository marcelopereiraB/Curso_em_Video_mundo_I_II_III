jogador = dict()
gols = list()

jogador['nome'] = str(input('nome da fera: '))
partidas = int(input('partidas jogadas: '))
for n in range(0, partidas):
    gol = int(input(f'quantos gols na partida {n+1}? '))
    gols.append(gol)
    jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for x, y in jogador.items():
    print(f'o campo {x} tem o valor {y}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for s, l in enumerate(gols):
    print(f'  => Na partida {s + 1}, fez {l} gols')
print(f'fez um total de {jogador["total"]} GOLS')

# curso em video
jog = dict()
parti = list()
jog['nome'] = str(input('nome do jogador: '))
tot = int(input(f'quantas partidas {jog["nome"]} jogou? '))
for c in range(0, tot):
    parti.append(int(input(f'   quantos gols na partida {c}')))
jog['gols'] = parti[:]
jog['total'] = sum(parti)
print('-='*30)
for k, v in jog.items():
    print(f' o campo {k} tem o valor {v}')
print('-='*30)
print(f'o jogador {jog["nome"]} jogou {len(jog["gols"])} partidas.')
for i, v in enumerate(jog['gols']):
    print(f'   => na partida {i}, fez {v} gols')
print(f'foi um total de {jog["total"]} gols.')
