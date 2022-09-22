from time import sleep


def lin():
    print('-=' * 30)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='')
        sleep(0.4)
    print('FIM!')


lin()
print('Contagem de lib até 10 de lib em lib')
contador(1, 11, 1)
lin()
print('contagem de 10 até 0 de 2 em 2')
contador(10, 0, -2)
print('Agora é sua ves de personalizar a contagem!')
ini = int(input('inicio: '))
fi = int(input('fim: '))
pas = int(input('passo: '))
if ini >= fi and pas != 0:
    contador(ini, fi, -pas)
lin()
print(f'a contagem de {ini} até {fi} de {pas} em {pas}!')


#modo curso em video
def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    lin()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    if i < f:
        conti = i
        while conti <= f:
            print(f'{conti} ', end='')
            sleep(0.5)
            conti += p
        print('FIM!!')
    else:
        conti = i
        while conti >= f:
            print(f'{conti} ', end='')
            sleep(0.5)
            conti -= p
        print('FIM!')


cont(1, 10, 1)
cont(10, 0, 2)
lin()
print('agora é sua vez de personalizar a contagem!')
inn = int(input('inicio: '))
fi = int(input('fim: '))
passs = int(input('passo: '))
cont(inn, fi, passs)
