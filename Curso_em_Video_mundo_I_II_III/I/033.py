#22
nome = str(input('Qual é o seu nome completo? ')).strip()
print('seu nome maiúsculo é {}'.format(nome.upper()))
print('seu nome minusculo é {}'.format(nome.lower()))
print('seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
#23
numero = int(input('Digite um numero de lib a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('analisando o número {}'.format(numero))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('Milhar: {}'.format(m))


#24
cidade = str(input('qual é o nome da sua cidade?')).strip()
print(cidade[:5].upper() == 'SANTO')
