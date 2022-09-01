al = float(input('digite sua altura: '))
pe = float(input('digite seu peso: '))
imc = pe / (al**2)
if imc <= 18.5:
    print(f'abaixo do peso ideal. {imc:.1f}')
elif 18.5 <= imc < 25:
    print(f'peso ideal, {imc:.1f}')
elif 25 <= imc < 30:
    print(f'sobre peso, {imc:.1f} ')
elif 30 <= imc < 40:
    print(f'obesidade, {imc:.1f} ')
else:
    print(f'obesidade morbida, {imc:.1f} cuidado macho')
