print('-'*50)
frase = 'LOJA SUPER BARATÃO'
print(frase.center(50))
print('-'*50)
total = total1 = menor = contador = 0
barato = ''
while True:
    produto = str(input('nome do produto: '))
    preco = int(input('Preço: R$'))
    contador += 1
    total = total + preco
    if preco > 1000:
        total1 += 1
    if contador == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total gasto foi R${total:.2f}')
print(f'{total1} produtos custam mais de R$1,000')
print(f'o produto mais barato foi {barato} que custa R${menor:.2f}')
