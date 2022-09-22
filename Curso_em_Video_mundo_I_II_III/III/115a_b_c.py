from centoE15.lib.interface import *
from centoE15.lib.arquivo import *
import time

arq = 'cursoemvideo.txt'


if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = Menu(['Ver pessoas cadastradas', 'Cadastra nova pessoa', 'sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        linha('NOVO CADASTRO')
        nome = str(input('nome: '))
        idade = leiaInt('idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        linha('saindo do sistema... até logo!')
        break
    else:
        print('\033[31merro! digite uma opção valida!\033[m')
    time.sleep(2)
