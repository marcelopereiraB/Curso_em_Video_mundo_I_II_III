def mostrarLinha(a):
    print('-' * len(a))
    print(f'{a}')
    print('-' * len(a))


mostrarLinha('ecommerce')
# rotina
a = 4
b = 5
s = a + b
print(s)
a = 8
b = 9
s = a + b
print(s)
a = 2
b = 1
s = a + b
print(s)


# resolvendo com def
def soma(a, b):
    s = a + b
    print(s)


mostrarLinha('resultado')
soma(a=4, b=5) # posso deixar explícito
soma(b=8, a=9)
soma(2, 1)

#empacotador em tupla
def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('fim')


contador(4, 5, 6, 7, 8, 2)
contador(1, 4)
contador(4, 5, 6, 9, 10)

#função com listas
valores = [7, 2, 5, 0, 4]


def dobra(lst):
   pos = 0
   while pos < len(lst):
    lst[pos] *= 2
    pos += 1


dobra(valores)
print(valores)


#desempacotar

def soma1(* valores):
    s = 0
    for num in valores: # para cada numero em valores
        s += num
    print(f'somando os valores de {valores} temos {s} ')


soma1(5, 2)
soma1(2, 9, 4)
