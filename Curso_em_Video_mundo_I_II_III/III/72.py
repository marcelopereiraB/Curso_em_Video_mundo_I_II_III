nume = ('zero', 'um', 'dois', 'três', 'quadro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'quatoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('digite um numero entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Digite novamente. Digite um numero entre 0 e 20: '))
print(f'você digitou o numero {nume[n]}')
