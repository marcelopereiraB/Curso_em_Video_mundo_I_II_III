#30
nu1 = int(input('saiba se o numero é par ou impar: '))
result = nu1 % 2
if result == 0:
    print('o numero {} par'.format(nu1))
else:
    print('o numero {} é impar'.format(nu1))
