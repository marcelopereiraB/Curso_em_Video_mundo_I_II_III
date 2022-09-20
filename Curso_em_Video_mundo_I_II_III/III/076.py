listagem = ('pão', 1.50,
            'peixe', 10,
            'abacaxi', 3,
            'banana', 2,
            'arroz', 4)
for iten in range(0, len(listagem)):
    if iten % 2 == 0:
        print(f'{listagem[iten]:.<30}', end=' ')
    else:
        print(f'R${listagem[iten]:>6.2f}')
