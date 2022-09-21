n1 = int(input('digite seu primeiro valor: '))
n2 = int(input('digite seu segundo valor: '))
v = 0
while v != 5:
    v = int(input('''
    [tamplate] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
     = '''))
    if v == 1:
        somar = n1 + n2
        print(f' a soma de {n1} e {n2} é {somar}')
    elif v == 2:
        multiplicar = n1 * n2
        print(f' a multiplicação de {n1}x{n2} é {multiplicar}')
    elif v == 3:
        if n1 > n2:
            print(f' o {n1} maior que {n2}')
        else:
            print(f' o {n2} maior que {n1}')
    elif v == 4:
        n1 = int(input('digite um novo valor: '))
        n2 = int(input('digite um novo valor: '))
    elif v == 5:
        print('obrigado, volte sempre!!!')
    else:
        print('opção invalida. tente novamente')
