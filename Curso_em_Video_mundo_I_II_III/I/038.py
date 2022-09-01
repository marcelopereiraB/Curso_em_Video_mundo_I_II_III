#29
vel = float(input('qual é a sua velocidade nessa estrada? '))
print('você foi multado'if vel >= 80.0 else 'está na velocidade normal da pista!')
# metodo 2
vel2 = float(input('qual é a sua velocidade nessa estrada? '))
if vel2 >= 80.0:
    print('você foi mutado!!!')
    multa = (vel2 - 80) * 7
    print('E o valor da sua multa é {}$'.format(multa))

else:
    print('está dentro da velocidade recomendada pra via!')
print('tenha um bom dia!! dirija com segurança!')
