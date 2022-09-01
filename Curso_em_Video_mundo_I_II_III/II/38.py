n1 = int(input('digite um numero: '))
n2 = int(input('digite um segundo numero: '))
if n1 > n2:
    print(f'o valor {n1} é maior que o {n2}')
elif n2 > n1:
    print(f'o valor {n2} é maior que o {n1}')
else:
    print(' não existe valor maior, os dois são iguas')
