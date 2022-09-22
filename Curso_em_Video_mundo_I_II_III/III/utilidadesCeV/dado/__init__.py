def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;30;41mERRO! \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


#113
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuario preferiu não digitar esse numero.')
            return 0
        else:
          return n




def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('o usuario preferiu não digitar um numero.')
            return 0
        else:
            return n

