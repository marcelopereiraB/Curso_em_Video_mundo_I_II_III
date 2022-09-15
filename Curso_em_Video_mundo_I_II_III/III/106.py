def manu():
    while True:
        print('-=' * 30)

        n = str(input('\033[0;49;32ma ajuda chegou, escreva um comando do Python que queira saber mais:\033[m ')).strip()
        help(n)
        v = str(input('\033[0;49;91mcaso queira sair do programa só digitar [Fim]\033[m  \033[0;49;32mCaso não ['
                      'continuar]:\033[m ')).strip().upper()[0]
        if v in 'F':
            print(f'\033[7;49;37mObrigado!')
            break

manu()


#modo curso em video

from time import sleep

c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30'        # 6 - branco
     );


def ajuda(com):
    titulo(f'acessando o manual do comando\'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA pyHELP', 2)
    comando = str(input("função ou biblioteca >"))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('até logo', 1)