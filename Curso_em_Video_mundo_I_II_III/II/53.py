frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #fatiou a str
junto = ''.join(palavras)# juntou todas desconsiderando os espaços
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('temos um palindromo!')
else:
    print('A frase dgitada não é um palíndromo!')