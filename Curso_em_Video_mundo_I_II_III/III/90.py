situ = dict()
nome = str(input('me diga seu nome? '))
media = float(input('qual é a sua média? '))
situ['nome_aluno'] = nome
situ['media'] = media
if situ['media'] >= 6:
    print(f'parabens {situ["nome_aluno"]} voce foi aprovado com uma media de {situ["media"]}')
else:
    print(f'infelizmente {situ["nome_aluno"]}, voce foi reprovado. com a media {situ["media"]}')
