# 31
from datetime import date

bi = int(input('digite um ano pra saber se é bissexto: '))
if bi == 0:
    bi = date.today().year
if bi % 4 == 0 and bi % 100 != 0 or bi % 400 == 0:
    print('{} é sim um ano Bissexto!!'.format(bi))
else:
    print('{} não é um ano bissexto'.format(bi))
