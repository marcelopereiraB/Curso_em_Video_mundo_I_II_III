def aumentar(n=0, por=0, formato=False):
    """

    :param n: numero para calculo
    :param por: a porcentagem que quer calcular
    :return: retorna o valor do calculo
    """
    g = n + (n * por / 100)
    return g if formato is False else moeda(g)


def diminuir(n=0, por=0, moeda=False):
    """

    :param n: numero par o calculo
    :param por: a porcentagem
    :return: retorna o valor
    """
    h = n - (n * por / 100)
    if moeda:
        return f'R${h:>.2f}'.replace('.', ',')
    return h


def dobro(n=0, formato=False):
    g = n * 2
    return g if formato is False else moeda(g)  # modo curso em video


def metade(n=0, formato=False):
    f = n / 2
    return f if formato is False else moeda(f)


def moeda(v=0, moeda='R$'):
    return f'{moeda}{v:>.2f}'.replace('.', ',')


def linha(msg):
    tam = len(msg) + 10
    print('-' * tam)
    print(f'{msg:>20}')
    print('-' * tam)


def resumo(valor, porcent1, porcent2, geral=False):
    print(f'Dobro do preço:  {dobro(valor, geral):>7}')
    print(f'Metade do preço: {metade(valor, geral):>7}')
    print(f'{porcent1:.0f}% de aumento:  {aumentar(valor, porcent1, geral):>7}')
    print(f'{porcent2:.0f}% de redução:  {diminuir(valor, porcent2, geral):>7}')
