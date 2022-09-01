n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite sua segunda nota: '))
media = (n1 + n2) / 2
print(f'tirando {n1:.1f} e {n2:.1f}, a media do aluno é {media:.1f}')
if media < 5:
    print('REPROVADO!!')
elif 7 > media >= 5:
    print('RECUPERAÇÃO!!')
    print(media)
elif media >= 7:
    print('APROVADO!!')
    print(media)
