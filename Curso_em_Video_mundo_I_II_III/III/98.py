from time import sleep

def lin():
    print('-=' * 30)


def contador(inicio, fim, passo):
    for c in range(inicio, fim, passo):
        print(f'{c} ', end='')
        sleep(0.4)
    print('FIM!')


lin()
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)
lin()
print('contagem de 10 até 0 de 2 em 2')
contador(10, 0, -2)
print('Agora é sua ves de personalizar a contagem!')
ini = int(input('inicio: '))
fi = int(input('fim: '))
pas = int(input('passo: '))
lin()
print(f'a contagem de {ini} até {fi} de {pas} em {pas}!')
if ini >= fi:
    contador(ini, fi, -pas)
if pas == 0:
    contador(ini, fi, 1)

