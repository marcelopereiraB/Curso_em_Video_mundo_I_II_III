from datetime import date
ano = date.today().year
contador1 = 0
contador2 = 0
for c in range(1, 8):
    n1 = int(input(f'em que ano a {c}a nasceu? '))
    result = ano - n1
    if result >= 21:
        contador1 += 1
    else:
        contador2 += 1
print(f'{contador1} pessoas atingiram a maior idade')
print(f'{contador2} pessoas não atingiram a maior idade')
