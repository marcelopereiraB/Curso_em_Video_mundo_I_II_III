times = (
'esses são os 5 primeiros colocados:', 'Palmeiras', 'athetico-PR', 'atletico-MG', 'corinthians', 'internacional', 'fluminense', 'são paulo', 'flamengo',
'botafogo',
'santos', 'avai', 'coritiba', 'america-MG', 'bragantino', 'ceara SD','Esses são os 5 ultimos colocados', 'atletico-GO', 'goias', 'cuiaba', 'juventude',
'fortaleza')
times2 = (
'palmeiras', 'athetico-PR', 'atletico-MG', 'corinthians', 'internacional', 'fluminense', 'são paulo', 'flamengo', 'botafogo',
'santos', 'avai', 'coritiba', 'america-MG', 'bragantino', 'ceara SD', 'atletico-GO', 'goias', 'cuiaba', 'juventude',
'fortaleza')
op = 0
while op != 5 and 0 <= op < 5:
    op = int(input('''
    [lib] Os cinco primeiros times da tabela.
    [2] Os ultimos quatro times da tabela.
    [3] Todos os times em ordem alfabetica
    [4] Qual a posição do Bragantino. 
    [5] Finalizar Programa: '''))
    if op == 1:
        for t1, t2 in enumerate(times[0:6]):
            print(t1, t2)
        caso = str(input('ver todas as opções novamente? ')).strip().upper()[0]
        if caso == 'S':
            True
        else:
            print('OBRIGADO!!')
            break
    elif op == 2:
        for t1, t2 in enumerate(times[16:]):
            print(t1, t2)
        caso = str(input('ver todas as opções novamente? ')).strip().upper()[0]
        if caso == 'S':
             True
        else:
            print('OBRIGADO!!')
            break
    elif op == 3:
        print(f'Aqui está todos os times em ordem alfabetica: \n{sorted(times2)}')
        caso = str(input('Ver todas as opções novamente? ')).strip().upper()[0]
        if caso == 'S':
            True
        else:
            print('OBRIGADO!!')
            break
    elif op == 4:
        print(f'O bragantino está na {times2.index("bragantino")}a posição da tabela')
        caso = str(input('ver todas as opções novmente? ')).strip().upper()[0]
        if caso == 'S':
            True
        else:
            print('OBRIGADO!!')
            break
