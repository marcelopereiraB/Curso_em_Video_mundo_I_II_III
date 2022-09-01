ca = float(input('qual é o valor do produto? '))
cartão = (ca + (ca * 5 / 100))
dinheiro = (ca - (ca * 10 /100))
print('O valor desse produto é R${}\n No cartão com acressimo de 8% fica R${:.5}\n Á vista com desconto de 10% é {:.5}'.format(ca, cartão, dinheiro))
