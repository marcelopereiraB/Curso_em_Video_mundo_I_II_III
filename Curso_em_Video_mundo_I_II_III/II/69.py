
frase = 'CADASTRE UMA PESSOA.'
print(frase.center(50))
v = c = z = 0
while True:
    idade = int(input('idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        v += 1
    if sexo == 'M':
        c += 1
    if sexo == 'F' and idade < 20:
        z += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'total de pessoas com mais de 18 anos: {v}')
print(f'Ao todo temos {c} homens cadastrados')
print(f'e temos {z} mulher com menos de 20 anos')
