from III.Modulos import moeda

p = float(input('digite o preço: R$ '))
por = float(input('digite a primeira porcentagem +: '))
por2 = float(input('digite a segunda porcentagem -: '))
moeda.linha('RESUMO DO VALOR')
moeda.resumo(p, por, por2, True)
print('-'*25)

