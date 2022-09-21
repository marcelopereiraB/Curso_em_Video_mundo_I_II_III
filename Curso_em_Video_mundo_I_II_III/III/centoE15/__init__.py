def linha(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


def menu():
    while True:
        try:
            linha('MENU PRINCIPAL')
            print('\033[1;92m1 -\033[m \033[1;34mVer pessoas cadastradas\033[m\n'
                  '\033[1;92m2 -\033[m \033[1;34mCadastrar nova pessoa\033[m\n'
                  '\033[1;92m3 -\033[m \033[1;34mSair do Sistema\033[m')
            print('-'*30)
            while True:
                op = int(input('\033[1;33mSua Opção:\033[m '))
                if op == 1:
                    linha('Opção 1')
                    break
                if op == 2:
                    linha('Opção 2')
                    break
                if op == 3:
                    linha('Saindo do sistema... até logo!')
                if 0 < op > 3:
                    print('erro! digite uma opção valida!')
                    break
        except (ValueError, TypeError):
            print('valor digitado invalido, por favor digite um valor correto')
        except (UnboundLocalError, KeyboardInterrupt):
            print('ERRO: valor não informado!')

            return op
