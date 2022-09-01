import random
from time import sleep

print('Pedra papel e tesoura!!')
sleep(1)
n = str(input('pedra, papel ou tesoura? ')).upper()
jokempo = ['PEDRA', 'PAPEL', 'TESOURA']
brink = random.choice(jokempo)
if brink == n:
    print('deu empate kkkkkk')
elif brink == 'TESOURA' and n == 'PAPEL':
    print('VOCE PERDEU KKKKK')
elif brink == 'PEDRA' and n == 'TESOURA':
    print('VOCE PERDEUUU LLKKKKK')
elif brink == 'PAPEL' and n == 'PEDRA':
    print('vc perdeu kkkkkkk')
elif n == 'TESOURA' and brink == 'PAPEL':
    print('VOCE GANHOUUUUU LKKKKK')
elif n == 'PEDRA' and brink == 'TESOURA':
    print('VC GANHOU KKKKKK')
elif n == 'PAPEL' and brink == 'PEDRA':
    print('VOCE GANHOU LLKKKK')
print(f'VC {n} o oponete {brink}')
print('fim de jogo!')

