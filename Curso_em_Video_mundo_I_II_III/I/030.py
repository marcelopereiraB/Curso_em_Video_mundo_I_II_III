from random import shuffle
name1 = str(input('primeiro aluno: '))
name2 = str(input('segundo aluno: '))
name3 = str(input('terceiro aluno: '))
name4 = str(input('quarto aluno: '))
lista = [name1, name2, name3, name4]
shuffle(lista)
print(' a ordem da lista sera ')
print(lista)
