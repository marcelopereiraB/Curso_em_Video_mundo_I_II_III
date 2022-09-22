#AULA 10
carro = int(input('quantos anos tem seu carro? '))
if carro <= 5:
    print('seu carro é bem novo em! só {} anos!'.format(carro))
else:
    print('seu carro é velho em kkkkkk')
print('--fim--'.center(35))
#exemplo lib
nome = str(input('Qual é seu nome? ')).upper().strip()
if nome == 'GUSTAVO':
    print('seu nome é sim {}, boa tarde meu amor'.format(nome))
else:
    print('nem te conheço, seu fudido')
print('fim'.center(25))
#exemplo 2
n1 = float(input('nota lib: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))
result = (n1 + n2 + n3 + n4) / 4
if result <= 5.6:
    print('você É BURRO EM MDS,\n REPROVOU!'.center(25))
else:
    print('você passou, parabens!!!! \n com a media: {:.2f}'.format(result))
