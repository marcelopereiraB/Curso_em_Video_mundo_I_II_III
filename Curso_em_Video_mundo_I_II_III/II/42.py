from time import sleep
print('-=-'*20)
print('Analisador de triangulos')
print('-=-'*20)
a = float(input('comprimento da primeira reta: '))
b = float(input('comprimento da segunda reta: '))
c = float(input('comprimento da terceira reta: '))
print('recolhendo informações...')
sleep(2)
if a + b > c and a + c > b and b + c > a:
    print('sim com essas medidas conseguimos fazer um triangulo', end=' ')
    if c == a == b:
        print('é um  triangulo equilatero')
    elif a != b != c != a:
        print('é um triangulo escaleno')
    else:
        print('é um triangulo isosceles')
else:
    print('não conseguimos fazer um triangulo')
