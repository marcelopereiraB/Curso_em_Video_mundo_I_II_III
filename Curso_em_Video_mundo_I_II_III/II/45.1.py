from random import randint
from time import sleep
itens = ('alguma ', 'PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''suas opções:
[ 1 ] PEDRA
[ 2 ] TESOURA
[ 3 ] PAPEL''')
jogador = int(input('qual é a sua jogada? '))
print('JO')
sleep(0.4)
print('KEN')
sleep(0.4)
print('PO')
print(f'computador jogou {itens[computador]}')
print(f'jogador jogou {itens[jogador]}')
if computador == 1:
    if jogador == 1:
        print('empate')
    elif jogador == 2:
        print('computador venceu')
    elif jogador == 3:
        print('player  venceu')
    else:
        print('PLAYER invalida!')
elif computador == 2:
    if jogador == 3:
        print('computador venceu!')
    elif jogador == 1:
        print('PLAYER venceu')
    elif jogador == 2:
        print('deu empate!')
    else:
        print('jogada invalida')
elif computador == 3:
    if jogador == 2:
        print('PLAYER venceu!')
    elif jogador == 1:
        print('computador venceu')
    elif jogador == 3:
        print('empate')
    else:
        print('jogada invalida!!')
