r = 'S'
maior = menor = media = contador = 0
while r in 'Ss':
    n1 = int(input('digite um numero: '))
    media += n1
    contador += 1
    if contador == 1:
       maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    r = str(input('Quer continuar? [S/N]? ')).upper().strip()[0]
mediageral = media / contador
print(f'a media dos numeros adicionados foi {mediageral:.2f} o numero maior foi {maior} e o menor foi {menor}')
