#interactive help
help(print) #documentação da função print
print(input.__doc__) # outra maneira de fazer a mesma coisa mas n é o mesmo texto


#Docstrings
def contador(i, f, p):
    """    #CRIANDO UMA DOCSTRING PARA A MINHA FUNÇÃO
    -> faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('fim')


contador(2, 10, 2)
help(contador)


#parametro opcinais
def somar(a=0, b=0, c=0): # c=0
    """
    -> soma dois ou 3 valores e mostra o resultado na tela>
    :param a: o primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: sem return
    """
    s = a + b + c
    print(f'a soma vale {s}')


#escopo de variaveis
def função():
    global a # se eu quiser decalara uma variavel global dentro de uma local
    a = 12 # como eu chamei a varaivel global, agora eu posso substituir o valor dentro dela
    print(a)


a = 2
função()
print(a)

#return de valores #retornar um valor para soma dentro do proprio programa obs. print n é retorno


def somar(a=0, b=0, c=0): # c=0
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(3, 6)
r3 = somar(10, 2, 1)

print(f'o resultado das somas serão {r1}, {r2} e {r3}')


#exercicio pratico
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'os resultados são {f1}, {f2} e {f3}')

#podemos retornar valores boleanos, tuplas, lista, dicionarios e muito mais
def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('digite um número: '))
r = par(num)
if r:
    print('parabnes')
else:
    print('não foi dessa vez')


# escopo de importação de biblioteca, economiza memoria


    def voto(nas=0):
        from datetime import date
        data = date.today().year - nas
        if 18 <= data < 70:
            print(f'Com {data} o voto é Obrigatorio.')
        elif 16 <= data < 18:
            print(f'com {data} o voto é Opcional')
        elif data < 16:
            print(f'com {data} não pode votar!')
        else:
            print(f'com {data} o voto é Opcional')

#valor literal == return