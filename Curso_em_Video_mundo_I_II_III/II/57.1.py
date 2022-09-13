'''for c in range(1, 10):
    print(c)
print('fim')'''
'''limite = 0
n = 0
while limite < 100:
    n = int(input('um valor: '))
    limite += n
print(f'voce chegou no seu limite de {limite}')'''
n = 1
'''while n:
    n = int(input('digite um numero: '))
    if n > 0:
        print('pode continuar')
    if n == 0:
        print('vc fez merda o p´rograma acabou')
n = 1
while n != 0:
    n = int(input('digite um numero: '))
print('fim')'''

'''r = 'S'
while r == 'S':
    n = int(input('digite um numero: '))
    r = str(input('quer continuar [S/N]? ')).upper()
print('fim')'''
'''lista = 0
maxime = 0
while maxime < 500:
    nome = str(input('me diga seu nome completo: ')).upper()
    lista = int(input('e seu nome na lista por favor: '))
    maxime = maxime + lista
    if nome in 'MARCELO PEREIRA':
        print(f'bem vindo {nome}')
    if maxime >= 500:
        print('todos os convidados estão na festa!')'''

'''n = 1
while n != 0:
    n = int(input('dgite um valor: '))
    if n % 2 == 0:
        print(f'o {n} é par')
    else:
        print(f'o {n} é impar')
print('cabo')'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'vc digitou {par} numeros par, e digitou {impar} numeros impar')
