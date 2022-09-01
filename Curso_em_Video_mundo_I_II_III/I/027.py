import math
nun = float(input('Qual é o valor do cateteo oposto:'))
nun2 = float(input('Qual é o valor do cateto adjacente: '))
nun3 = math.hypot(nun, nun2)
print('O valor da hipotenusa é: {:.2f}'.format(nun3))
# maneira 1
from math import hypot
ca = float(input('qual é o valor do cateto oposto: '))
co = float(input('qual é o valor do cateto adjacente: '))
hi = hypot(ca, co)
print('o valor da hipotenusa é {:.2f}'.format(hi))



