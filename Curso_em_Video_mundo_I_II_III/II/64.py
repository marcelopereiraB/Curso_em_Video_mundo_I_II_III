n = somar = contador = 0
while n != 999:
    n = int(input('digite um numero: '))
    if n != 999:
        contador += 1
        somar += n
print(f'vc digitou {contador} numeros e a soma deles é {somar}')
