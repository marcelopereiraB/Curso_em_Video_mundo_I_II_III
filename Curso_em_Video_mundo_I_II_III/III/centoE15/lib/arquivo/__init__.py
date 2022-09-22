def linha(msg):
    print('-' * 30)
    print(msg.center(30))
    print('-' * 30)


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #r = head, t = text, w = escrever, + = se não tiver ele cria.
        a.close()
    except:
        print('houve um erro na criação do arquivo!')
    else:
        print(f'arquivo {nome} criado com sucesso!')


#como ler arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler arquivo')
    else:
        linha('PESSOAS CADASTRADAS')
        for lin in a:
            dado = lin.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('houve erro na hora de escrever os dados!')
        else:
            print(f'novo registro de {nome} adicionado.')
            a.close()
