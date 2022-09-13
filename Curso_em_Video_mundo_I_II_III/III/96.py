def area(b, h):
    cal = b * h
    print(f'A área de um terreno {b}x{h} é de {cal:.1f}m2.')


print('controle de terrenos')
print('-'*20)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
