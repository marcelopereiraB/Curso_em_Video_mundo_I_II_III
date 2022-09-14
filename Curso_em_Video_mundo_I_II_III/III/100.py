from random import randint
nunu = []


def sorteio(nu):
    números = [randint(0, 20), randint(10, 30), randint(20, 40), randint(40, 60), randint(10, 30)]

    nu.append(números[:])


def somaPar(a):
    soma = 0
    for c in a:
        if c % 2 == 0:
            soma += c
    print(soma)
    print(a)


sorteio(nunu)
somaPar(nunu)
