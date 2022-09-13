# aula 12
nome = str(input('me diga seu nome? '))
if nome == 'Gustavo':
    print('que nome bonito um bom dia')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Páulo':
    print('seu nome é bem popular no brasil')
elif nome in 'Ana caludia jesica  juliana':
    print('belo nome feminino')
else:
    print('seu nome é bem normal')
print('bom dia')
