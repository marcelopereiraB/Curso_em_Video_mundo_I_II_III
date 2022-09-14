from random import randint
from time import sleep


def sorteio(lista):
    print('sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somaPar(a):
    soma = 0
    for c in a:
        if c % 2 == 0:
            soma += c
    print(f'A somando todos os valores pares da lista {a}, o resultado é {soma}')


list = list()
sorteio(list)
somaPar(list)

