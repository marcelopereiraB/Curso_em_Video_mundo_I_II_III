n = int(input('digite o primeiro termo: '))
r = int(input('digite a razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -', end='')
        termo += r
        cont += 1
    print('pausa')
    mais = int(input('quantos termos voce quer mostar a mais? '))
print(f'progreção finalizada com {total} termos')







