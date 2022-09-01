s = contador = 0
while True:
    n = int(input('digite um numero (999 para parar): '))
    if n == 999:
        break
    s += n
    contador += 1
print(f'Com o tatal de {contador} numeros digitados, a soma de todos é {s}')
