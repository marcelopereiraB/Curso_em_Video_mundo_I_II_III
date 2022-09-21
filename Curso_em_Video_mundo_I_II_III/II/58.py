# maneira tamplate
import random
m = random.randint(1, 10)
c = 0
contador = 1
while m != c:
    c = int(input('digite um número: '))
    if m == c:
        print(f'vc acetou!!! a maquina jogou {m}, o mesmo numero que vc. vc tentou {contador} vezes')
    contador = contador + 1
    if m != c:
        print('vc ERROU, tente novamente!')

#maneira 2
from random import randint
computador = randint(0, 10)
palpites = 0
print('sou seu computador... acabei de pensar em um nuemro entre 0 e 10.')
print('será que vc consegue adivinhar qual é???')
acertou = False
while not acertou:
    jogador = int(input('qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('um valor maior em...')
        elif jogador > computador:
            print('um valor menor em...')
print(f'acertou!!! com {palpites} palpites, parabens')
