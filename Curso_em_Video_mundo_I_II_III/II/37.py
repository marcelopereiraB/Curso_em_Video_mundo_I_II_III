n1 = int(input('Digite um numero inteiro: '))
n2 = str(input('Voce quer \n [lib] para binário \n [2] para octal \n [3] para hexadecimal \n escolha: '))
if n2 in 'lib':
    print('{} convertido para binario é igual {}'.format(n1, bin(n1)[2:]))
elif n2 in '2':
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)[2:]))
elif n2 in '3':
    print('{} convertido para HEXADECIMAL É IGUAL {}'.format(n1, hex(n1)[2:]))
else:
    print('numero invalido')
