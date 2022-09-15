
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


print('-'*30)
n = leiaInt('digite um número: ')
print(f'voce acabou de digitar o numero {n}')
