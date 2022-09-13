from random import choice
m = str(input('Qual rota? '))
M = str(input('Qual é seu nome? '))
rota1 = ['diana', 'Darius', 'Malphate', 'Olaf']
rota2 = ['pyke', 'evellyn', 'aphelios', 'sivir']
result = choice(rota1)
print('Seu boneco é {}'.format(result))
