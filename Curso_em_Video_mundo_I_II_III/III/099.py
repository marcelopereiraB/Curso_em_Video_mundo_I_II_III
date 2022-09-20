from time import sleep


def lin():
    print('-='*30)


def maior(*n):
    mama = max(n)
    print('Analisando os valores passados...')
    cont = 0
    for c in n:
        print(f'{c} ', end='')
        sleep(0.5)
        cont += 1
    print(f'foram imformados {cont} valores ao todo.')
    print(f'O maior valor imformado foi {mama}.')


lin()
maior(2, 9, 4, 5, 7, 1)
lin()
maior(4, 7, 0)
lin()
maior(1, 2)
lin()
maior(6)
lin()

#modo curso em video
def maiorr(*num):
    cont = maior = 0
    lin()
    print('analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'foram imformados {cont} valores ao todo.')
    print(f'O maior valor imformado foi {maior}.')


lin()
maiorr(2, 9, 4, 5, 7, 1)
lin()
maiorr(4, 7, 0)
lin()
maiorr(1, 2)
lin()
maiorr(6)
lin()
maiorr()


