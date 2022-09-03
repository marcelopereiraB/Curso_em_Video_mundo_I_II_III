jogador = dict()
gols = list()
cont = 0
jogador['nome'] = str(input('nome da fera: '))
partidas = int(input('partidas jogadas: '))
for n in range(0, partidas):
    gol = int(input(f'quantos gols na partida {n}? '))
    gols.append(gol)
    cont += gol
    jogador['gols'] = gols
jogador['total'] = cont
print('-='*30)
print(jogador)
print('-='*30)
for x, y in jogador.items():
    print(f'o campo {x} tem o valor {y}.')
print('-='*30)
print(f'O jogador jogou {partidas} partidas.')
for s, l in enumerate(gols):
    print(f'  => Na partida {s}, fez {l} gols')
print(f'fez um total de {jogador["total"]} GOLS')

