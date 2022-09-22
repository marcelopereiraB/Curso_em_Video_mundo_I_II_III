alunos = list()
while True:
    nome = str(input('nome: '))
    nota1 = float(input('nota lib: '))
    nota2 = float(input('nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    s = str(input('quer continuar? [S/N]')).strip()[0]
    if s in 'Nn':
        break
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 25)
    m = int(input('mostar notas de qual aluno? (999 interrompe): '))
    if m == 999:
        print('finalizando...')
        break
    if m <= len(alunos) - 1:
        print(f'notas do {alunos[m][0]} são {alunos[m][1]} ')
print('volte sempre')
print(alunos)
