def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')


name = str(input('nome do jogador: '))
number = str(input('numero de gols: '))
if number.isnumeric():
    number = int(number)
else:
    number = 0
if name.strip() == '':
    ficha(gol=number)
else:
    ficha(name, number)

