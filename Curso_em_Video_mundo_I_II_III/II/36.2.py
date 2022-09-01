from time import sleep

print('seu imprestimos bancarios é aqui!!! VEM!!')
sleep(1)
din = float(input('Qual é o valor da casa? '))
sa = float(input('Qual é o seu salario? '))
ano = int(input('Em quantos anos  quer pagar o imovel? '))
pres = (din / ano) / 12
po = sa - (sa * 70 / 100)
if pres <= po:
    print('Voce tem condiçoes para efetuar a compra do imovel, parabens!!!')
    sleep(1)
    print(f'suas parcelas ficaram no valor de R${pres:.2f},', end=' ')
    print(f'emprestimo concedido')
else:
    print('infelizmente não podemos te ajudar, EMPRESTIMO NEGADO!')
