import random
name1 = str(input('Primiero aluno: '))
name2 = str(input('segundo aluno: '))
name3 = str(input('Terceiro aluno: '))
name4 = str(input('Quarto aluno: '))
lista = [name1, name2, name3, name4]
resultado = random.choice(lista)
print('O aluno escolhido foi {}'.format(resultado))

# outra forma
from random import choice
name= str(input('Priemiro aluno: '))
name2 = str(input('Segundo aluno: '))
name3 = str(input('Terceiro aluno: '))
name4 = str(input('Quarto aluno: '))
lista = [name, name2, name3, name4]
escolhido = choice(lista)
print('o escolhido foi {}'.format(escolhido))

