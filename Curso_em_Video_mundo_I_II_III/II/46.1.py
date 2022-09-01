# aula 13
for c in range(0, 7, 2): #iteração
    print(c)
print('fim')

i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo'))
for c in range(i, f+1, p):
    print(c)
s = 0
for c in range(0, 3):
    n = int(input('digite um valor: '))
    s += n
print(f'fim, {s}')
