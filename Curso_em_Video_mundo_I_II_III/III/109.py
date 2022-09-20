from utilidadesCeV import moeda

valor = float(input('qual é o valor para os demais calculos: '))
por = float(input('digite quantos porcentos quer tirar do seu valor: '))
por2 = float(input('digite quantos porcento quer adicionar no seu valor: '))

print(f'diminuindo {por}% de {moeda.moeda(valor)} o valor fica {moeda.diminuir(valor, por, True)} ')
print(f'aumentando {por2}% de {moeda.moeda(valor)} o valor fica {moeda.aumentar(valor, por2, True)} ')
print(f'o dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)} ')
print(f'a metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)} ')
