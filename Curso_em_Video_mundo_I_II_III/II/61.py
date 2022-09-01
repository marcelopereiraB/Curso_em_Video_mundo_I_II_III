
n = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
termo = n
cont = 1
while cont <= 10:
    print(f'{termo} -', end='')
    termo += r
    cont += 1
print('fim')
