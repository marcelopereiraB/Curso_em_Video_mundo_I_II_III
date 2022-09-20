dados = dict()
dados = {'nome': 'pedro', 'idade': 25}
print(dados['nome'], dados['idade'])
dados['sexo'] = 'm' # add
dados['peso'] = 120 # add
print(dados)
del dados['idade'] # deletar um dado
dados['nome'] = 'marcelo' #substituindo
print(dados)
filme = {'Titulo': 'Star wars',
         'ano': 1977,
         'diretor': 'George Lucas'}
print(filme.values()) # pega só os valores/dados, como star wars, 1977 etc...
print(filme.keys()) # pega os index/chaves as palavras chaves do dicionário.
print(filme.items()) # pega tudo, tanto chaves quanto  valor.
for k, v in filme.items():
    print(f'o {k}, é o index e o {v} é o valor dentro da chave')
locadora = [{'Titulo': 'Star wars',
             'ano': 1977,
             'diretor': 'George Lucas'},
            {'Titulo': 'avengers',
             'ano': 2012, 'diretor': 'Joss Whedon'},
            {'Titulo': 'matrix',
             'ano': 1999,
             'diretor': 'wachowki'}]
for c, l in enumerate(locadora):
    print(locadora[c]['diretor'], l)
#pratica
pessoas = {'nome': 'marcelo', 'sexo': 'M', 'idade': 21}
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')
for k, v in pessoas.items():
    print(f'{k} = {v} ')
brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'rj'}
estado2 = {'uf': 'são paulo', 'sigla': 'sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['sigla'])
est = dict()
brasi = list()
for c in range(0, 3):
    est['uf'] = str(input('unidade federativa: '))
    est['sigla'] = str(input('sigla do estado: '))
    brasi.append(est.copy())
for e in brasi:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
