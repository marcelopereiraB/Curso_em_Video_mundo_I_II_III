from uteis import números

num = int(input('digite um valor: '))
fat = números.fatorial(num)
print(f'o fatorial de {num} é {fat}')
print(f'dobro de {num} é {números.triplo(num)}.')
print(f'o triplo de {num} é {números.dobro(num)}')


