#len
frase = 'I am Iron man bitch'
print(len(frase))
#count
frase = 'I am Iron man bitch'
b = frase.count('I')
print(b)
#find
frase = 'I am Iron man bitch'
c = frase.find('m')
print(c)
#replace
frase = 'I am Iron man bitch'
d = frase.replace('I am', 'I you')
print(d)
#upper
frase = 'I am Iron man bitch'
e = frase.upper()
f = frase.lower()
print(e, f)
#capitalize
frase = 'I am Iron man bitch'
g = frase.capitalize()
print(g)
#title
frase = 'I am Iron man bitch'
h = frase.title()
print(h)
#strip
frase = '       I am Iron man bitch      '
i = frase.strip()
j = frase.rstrip()
k = frase.lstrip()
print(i)
print(j)
print(k)
#split
frase = 'I am Iron man bitch'
l = frase.split()
print(l)
#join
frase = 'I am Iron man bitch'
m = frase.splitlines()
n = ' '.join(frase)
print(m, n)

#obs = como escrever texto maiores: """
print("""Porque eu amo você texto?
Você é maravilhosa e tudo o que 
há de melhor neste mundo, será sempre pouco para você.
Eu tudo vou fazer sempre para que você realize todos os seus sonhos e seja muito feliz.
E enquanto você estiver ao meu lado, a minha felicidade está garantida. Amo a vida, amo viver, e tudo porque amo você""")
# in
frase = 'I am Iron man bitch'
b = input('digite alguima merda: ')
a = frase.replace('I am', b)
print(a)
#in
frase = 'I am Iron man bitch'
print('I am Iron man' in frase)
#split
frase = 'I am Iron man bitch'
yu = frase.split()
print(yu[2][1])
