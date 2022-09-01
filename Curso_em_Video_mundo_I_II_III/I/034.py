#25
nome = str(input('qual é seu nome completo? ')).strip()
print('seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
#26
frase = str(input('digite uma frase: ')).upper().strip()
print('quantas vezes a parece a letra A: {}'.format(frase.count('A')))
print('sua primeira posição:', frase.find('A'))
print('a ultima letra A apareceu na posição {}'.format(frase.rfind('A')))
z = frase
print(z)

