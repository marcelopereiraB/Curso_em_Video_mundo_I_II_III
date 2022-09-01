# 33
n1 = int(input('digite o primeiro número:'))
n2 = int(input('digite o segundo número:'))
n3 = int(input('digite o terceiro número:'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n2
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
print('o maior valo digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
