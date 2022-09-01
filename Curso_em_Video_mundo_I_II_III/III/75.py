def funcao():
    return int(input('insira um numero: '))


tupla = (funcao(), funcao(), funcao(), funcao())
print(tupla)

if 9 in tupla:
    print(f'O numero 9 apareceu {tupla.count(9)} vezes')
else:
    print('o numero 9 não apareceu nenhuma vez.')
if 3 in tupla:
    print(f'a primeira ocorrencia do numero 3 é na posição {tupla.index(3)}')
else:
    print('não houve ocorrencia do numero 3.')
print(f'os valores pares digitados foram ', end='')
for t in tupla:
    if t % 2 == 0:
        print(t, end=' ')


#2 forma
num = (int(input('\ndigite um número: ')),
        int(input('digite um número: ')),
        int(input('digite um número: ')),
        int(input('digite um número: ')))
print(f'vc digitou os valores {num}')
print(f' o valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'o valor 3 apareceu {num.index(3)}a posição')
else:
    print('numero 3 não existente')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')