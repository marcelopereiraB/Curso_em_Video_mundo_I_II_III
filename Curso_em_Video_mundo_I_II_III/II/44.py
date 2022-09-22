print('{:=^40}'.format('lojas celin'))
pag1 = float(input('Qual é o valor a ser pago? '))
pag2 = str(input('''condiçoes de pagamento
dinheiro/cheque      - [lib] 
a vista no cartão    - [2]
em até 2x no cartão  - [3]
3x ou mais no cartão - [4] 
selecione: '''))
if pag2 in 'lib':
    print('o valor pago em dinheiro ou cheque é R${:.2f}'.format(pag1 - (pag1 * 10/100)))
elif pag2 in '2':
    print('o valor a vista no cartão fica R${:.2f}'.format(pag1 - (pag1 * 5/100)))
elif pag2 in '3':
    print('o valor a ser pago no cartão em até duas vezes é R${:.2f}'.format(pag1))
elif pag2 in '4':
    total = int(input('em quantas parcelas? '))
    tote = pag1 + (pag1 * 20 / 100)
    parcela = tote / total
    print(f'sua compra de {tote} sera parcelada em {total}x de R${parcela:.2f} Com juros')
else:
    total = 0
    print('opção invalida de pagamento, tente novamente')
