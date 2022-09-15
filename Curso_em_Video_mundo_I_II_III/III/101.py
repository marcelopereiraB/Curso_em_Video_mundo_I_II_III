#escopo de importação de biblioteca, economiza memoria


def voto(nas=0):
    from datetime import date
    data = date.today().year - nas

    if 16 <= data < 18 or data > 65:
        return f'com {data} o voto é Opcional'
    elif data < 16:
        return f'com {data} não pode votar!'
    else:
        return f'Com {data} o voto é Obrigatorio.'


print('-' * 30)
ano = int(input('digite o ano de seu nascimento: '))
print(voto(ano))

