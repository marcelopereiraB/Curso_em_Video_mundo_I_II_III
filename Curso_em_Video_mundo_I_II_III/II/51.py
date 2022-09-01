n = int(input('digite o primeiro termo: '))
r = int(input('digite um numero para a razão: '))
decimo = n + (10 -1) * r
for c in range(n, decimo + r, r):
    print(c)
