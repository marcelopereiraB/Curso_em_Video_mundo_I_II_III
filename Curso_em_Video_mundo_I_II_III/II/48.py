soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
print(f'a soma de todos sos numeros impares divisivos por 3 são {soma} com {contador} valores')
