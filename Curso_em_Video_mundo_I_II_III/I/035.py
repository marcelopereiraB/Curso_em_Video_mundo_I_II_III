#27
nome = str(input('seu nome completo: ')).upper().strip()
nome = nome.split()
print('seu primiero nome é nome {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
