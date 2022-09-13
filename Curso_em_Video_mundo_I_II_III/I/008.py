n = int(input('um valor:'))
n1 = int(input('outro valor: '))
s = n + n1
m = n * n1
d = n / n1
p = n ** n1
g = n // n1
j = n % n1
print('A soma vale {}, \n o produto é {} e a divisão é {:.3f}'.format(s,m,d),end=' ')
print('A potencia é {}, o inteiro {} e o resto da divisão {}'.format(p,g,j))
