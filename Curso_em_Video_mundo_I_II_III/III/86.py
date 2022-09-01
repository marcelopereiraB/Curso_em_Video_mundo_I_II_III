matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): # esse é responsavel por entrar dentro da linha
    for c in range(0, 3): # esse é responsavel por preencher as colunas dessa linha
        matriz[l][c] = int(input(f'digite um valor para [{l}, {c}]:')) # adiciona ma matriz não com uma função  mais com com a referencia do idez matriz[][]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
