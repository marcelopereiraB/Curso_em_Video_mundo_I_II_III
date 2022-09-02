from random import randint
from time import sleep
joga = {'jogador 1': randint(1, 7),
        'jogador 2': randint(1, 7),
        'jogador 3': randint(1, 7),
        'jogador 4': randint(1, 7)}
print('valores sorteados:')
maior = joga['jogador 1']
print(f' o jogador1 tirou {maior}')
if joga['jogador 1'] <= joga['jogador 2'] >= joga['jogador 3'] and joga['jogador 2'] >= joga['jogador 4']:
    maior = joga['jogador 2']
print(f' o jogador2 tirou {maior}')
if joga['jogador 1'] <= joga['jogador 3'] >= joga['jogador 2'] and joga['jogador 3'] >= joga['jogador 4']:
    maior = joga['jogador 3']
print(f' o jogador3 tirou {maior}')
if joga['jogador 2'] <= joga['jogador 4'] >= joga['jogador 3'] and joga['jogador 4'] >= joga['jogador 1']:
    maior = joga['jogador 4']
print(f' o jogador4 tirou {maior}')





