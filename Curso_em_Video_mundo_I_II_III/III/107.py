from III.Modulos import moeda

valor = float(input('qual é o valor para os demais calculos: '))
por = float(input('digite quantos porcentos quer tirar do seu valor: '))
por2 = float(input('digite quantos porcento quer adicionar no seu valor: '))

print(f'diminuindo {por}% de R${valor} o valor fica R${moeda.diminuir(valor, por)}.')
print(f'aumentando {por2}% de R${valor} o valor fica R${moeda.aumentar(valor, por2)}.')
print(f'o dobro de R${valor} é R${moeda.dobro(valor):.1f}.')
print(f'a metade de R${valor} é R${moeda.metade(valor)}.')
