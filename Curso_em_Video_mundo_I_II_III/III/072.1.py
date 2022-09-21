lanches = ('Hamburgues', 'Suco', 'Pizza', 'Pudim', 'MilkShake')
#tamplate
for c in lanches:
    print(f'eu como {c}')

#tamplate.2
for c in lanches:
    if c == lanches[1] or c == lanches[4]:
        print(f'eu vou tomar {c}')
    else:
        print(f'eu vou comer {c}')
print('comi muito emmmmmmm')

#2
for cont in range(0, len(lanches)):
    print(lanches[cont], cont)
    #enumerate = criando outra varia no laço for pode-se enumerar os indices

#3
for vip, comida in enumerate(lanches):
    print(f'seu dado armazenado na posição {vip} é {comida}')
#sorted = organizado
print(sorted(lanches))

#função index = indice
c = (1, 2, 3, 5)
v = (2, 3, 6, 5)
x = c + v
print(x.count(6))
print(x)
print(x.index(5), x.index(5, 4))
