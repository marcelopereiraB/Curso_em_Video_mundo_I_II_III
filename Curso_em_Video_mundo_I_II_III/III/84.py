#minha versão
matricula_acad = list()
peso_maior = list()
menor_peso = list()
maior = 0
menor = 0
cont = 0
nome = None
nome2 = None
while True:
    matricula_acad.append(str(input('Nome: ')))
    matricula_acad.append(float(input('Peso atual: ')))
    sim = str(input('quer contiuar a cadastrar pessoas? [S/N] '))
    cont += 1
    menor_peso.append(matricula_acad[:])
    peso_maior.append(matricula_acad[:])
    matricula_acad.clear()
    menor = menor_peso[0][1]
    if menor_peso[cont - 1][1] < menor:
        menor = menor_peso[cont - 1][1]
        nome2 = menor_peso[cont - 1][0]
    if peso_maior[cont - 1][1] > maior:
        maior = peso_maior[cont - 1][1]
        nome = peso_maior[cont - 1][0]
    if sim in 'Nn':
        print('Obrigado')
        break

print(f'o total de pessoas cadastradas hj foram {cont}')
print(f'a pessoa mais pesada cadastrada hj é {nome} com o peso de {maior}')
print(f'a pessoa com menor peso cadastrada hj foi {nome2} com o peso de {menor}')

 #versão curso em video
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('nome: ')))
    temp.append(float(input('peso: ')))
    if len(princ) == 0:
        maior = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'ao todo vc cadastrou {len(princ)} pessoas.')
print(f'o maior peso foi de {mai}kg. peso de ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'o menor peso foi de {men}kg. peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
print()
