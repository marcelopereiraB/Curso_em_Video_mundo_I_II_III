from random import randint
from time import sleep
lista = list()
jogos = list()

sort = int(input('quantos números voce quer sortear? '))
total = 1
while total <= sort:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for i, l in enumerate(jogos):
    print(f'jogo {i}: {l}')
    sleep(1)




