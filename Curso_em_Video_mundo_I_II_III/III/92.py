info = dict()
info['nome'] = str(input('digite seu nome: '))
info['nascimento'] = int(input('digite seu ano de nascimento: '))
info['carteira'] = int(input('carteira de trabalho (0 não tem): '))
info['idade'] = 2022 - info['nascimento'] # 35 anos de colaboração
if info['carteira'] != 0:
    info['contratação'] = int(input('ano de contratação: '))
    info['salário'] = float(input('salário: R$ '))
    info['contribuição'] = 2021 - info['contratação']
print('-=' * 30)
for c, v in info.items():
    print(f'{c} tem o valor {v}')
if info['carteira'] != 0:
    if info['contribuição'] > 35:
        print('voce  ja pode se aposentar')
    else:
        print(f'vc ainda não pode se aposentar faltam {35 - info["contribuição"]} anos de contribuição')

