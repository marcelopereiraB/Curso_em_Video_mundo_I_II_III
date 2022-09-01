soma = 0
contador = 0
for c in range(1, 7):
    name = int(input(f'digite o {c} número: '))
    if name % 2 == 0:
        soma += name
        contador += + 1
print(f'voce adicionou {contador} numeros pares, e a soma deles é {soma}')

