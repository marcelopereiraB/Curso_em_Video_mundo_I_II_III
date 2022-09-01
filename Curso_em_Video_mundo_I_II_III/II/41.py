from datetime import date

nas = int(input('digite seu ano de nasciemnto: '))
ano = date.today().year
cal = ano - nas
if cal <= 9:
    print(f'com {cal} anos, sua categoria é a mirim')
elif cal <= 14:
    print(f'com {cal} anos, sua categoria é infantil')
elif cal <= 19:
    print(f'com {cal} anos, sua categoria é junior')
elif cal <= 25:
    print(f'com {cal} anos, sua categoria é senior')
else:
    print('sua categoria é master')
