while True:
    nu = int(input('digite um numero para fazermos sua tabuada: '))
    if nu < 0:
        break
    for c in range(1, 11):
        mult = nu * c
        print(f'{nu} X {c} = {mult}')
print('programa finalizado, obrigado <3')






