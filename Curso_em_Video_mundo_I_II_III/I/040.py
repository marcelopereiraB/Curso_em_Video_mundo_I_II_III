#31
dis = float(input('qual é a distancia em kl da sua viagem? '))
if dis <= 200.0:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
