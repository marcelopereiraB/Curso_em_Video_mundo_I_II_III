#34
salario = float(input('digite seu salario pra saber se recebera um aumento: '))
if salario <= 1.250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('seu novo salario será R${}'.format(novo))

