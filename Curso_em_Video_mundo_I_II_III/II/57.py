#maneira tamplate
m = ''
f = ''
add = ''
while m != 'M' or m != 'F':
    m = str(input('digite seu sexo [M/F]? ')).strip().upper()[0]
    idade = int(input('digite sua idade? '))
    if m not in 'FM':
        print('esta errado, digite novamente por favor')
    if m == 'M' or m == 'F':
        print('esta correta a informação recolhida!')

#maneira 2
sexo = str(input('digite seu sexo [S/M]')).strip().upper()[0]
while sexo not in 'MFmf':
    sexo = str(input('dados invalidos. por favor, informe seu sexo: ')).strip().upper()[0]
iden = int(input('digite sua idade: '))
print(f'sexo {sexo} registrado com sucesso')
