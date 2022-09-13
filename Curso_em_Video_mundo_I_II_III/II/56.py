somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher20 = 0
for c in range(1, 5):
    nome = str(input('qual é seu nome? ')).strip()
    idade = int(input('qual é a sua idade? '))
    sexo = str(input('sexo [M/F]')).strip().upper()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediaidade = somaidade / 4
print(f'A media de idade do grupo é de {mediaidade}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'são {mulher20} mulheres com menos de 20 anos')
