pro = float(input('qual é o preço do produto? '))
des = pro - (pro * 20 / 100)
print('o pruduto que custava {} vai sair em pormoção com desconto de 20% por R${:.3}'.format(pro, des))
