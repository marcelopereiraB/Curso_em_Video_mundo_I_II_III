situ = dict()
nome = str(input('me diga seu nome? '))
media = float(input('qual é a sua média? '))
situ['nome_aluno'] = nome
situ['media'] = media
if situ['media'] >= 6:
    print(f'parabens {situ["nome_aluno"]} voce foi aprovado com uma media de {situ["media"]}')
else:
    print(f'infelizmente {situ["nome_aluno"]}, voce foi reprovado. com a media {situ["media"]}')

#CURSO EM VIDEO

aluno = dict()
aluno['nome'] = str(input('nome: '))
aluno['media'] = float(input(f'média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
