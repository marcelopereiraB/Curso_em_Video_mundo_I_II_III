from utilidadesCeV import moeda

valor = float(input('qual é o valor para os demais calculos: '))
por = float(input('digite quantos porcentos quer tirar do seu valor: '))
por2 = float(input('digite quantos porcento quer adicionar no seu valor: '))

print(f'diminuindo {por}% de {moeda.moeda(valor)} o valor fica {moeda.moeda(moeda.diminuir(valor, por))} .')
print(f'aumentando {por2}% de {moeda.moeda(valor)} o valor fica {moeda.moeda(moeda.aumentar(valor, por2))} .')
print(f'o dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))} .')
print(f'a metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))} .')
