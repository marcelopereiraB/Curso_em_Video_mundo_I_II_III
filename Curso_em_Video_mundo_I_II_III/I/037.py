#28
from random import choice
from time import sleep
numero = int(input('descubra o número que o pc escolheu de 0 a 5: '))
lista = [1, 2, 3, 4, 5]
pc = choice(lista)
print('PROCESSANDO...')
sleep(1)
if pc == numero:
    print('você acertou!!! o numero foi {}'.format(pc))

else:
    print('tu errou tente novamente!')
    print('o numero escolhido foi {}'.format(pc))


