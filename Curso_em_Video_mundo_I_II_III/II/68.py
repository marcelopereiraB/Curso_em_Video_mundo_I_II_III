# meu jeito
import random
while True:
    n = int(input('jogue um numero: '))
    i = str(input('impar ou par [I/P]')).upper().strip()[0]
    pc2 = random.randint(1, 10)
    soma = pc2 + n
    lista = ['P', 'I']
    pc = random.choice(lista)
    if soma % 2 == 0 and i in 'Ii' and pc == 'I':
        print(f'os dois escolheram impar, com o total de  {soma} - Os dois perderam')
        break
    elif soma % 2 == 0 and i in 'Pp' and pc == 'P':
        print(f'Houve um empate a soma dos numeros foi {soma} - Os dois jogaram Par')
        print('continue')
    elif soma % 2 == 0 and i in 'Pp' and pc == 'I':
        print(f'vc ganhou, a soma dos numeros foi {soma} - O pc escolheu Impar')
        print('continue...')
    elif soma % 2 == 0 and i in 'Ii' and pc == 'P':
        print(f'computador ganhou, com o valor total de {soma} - Jogador escolheu Impar')
        break
    elif soma % 2 != 0 and i in 'Ii' and pc == 'P':
        print(f'jogador ganhou, com o valor total de {soma} - Pc jogou Par ')
        print('continue')
    elif soma % 2 != 0 and i in 'Pp' and pc == 'I':
        print(f'voce perdeuuu, com o valor total de {soma} - Jogador escolheu Par')
        break
    elif soma % 2 != 0 and i in 'Pp' and pc == 'P':
        print(f'os dois perderam, com o valor total de {soma} - Os dois jogaram Par')
        break
    elif soma % 2 != 0 and i in 'Ii' and pc == 'I':
        print(f'houve um empate, com o valor total de {soma} - os dois jogaram Impar')
        print('continue')
# curso em video
from random import randint
v = 0
while True:
    jogador = int(input('diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('par ou impar? [P/I] ')).strip().upper()[0]
        print(f'vc jogou {jogador} e o computador {computador}. total de {total}')
        print('deu par' if total % 2 == 0 else 'deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('vc venceu!')
            v += 1
        else:
            print('vc perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('vc venceu!')
            v += 1
        else:
            print('vc perdeu!')
            break
    print('vamos jogar novamente...')

print(f'vc venceu {v}')