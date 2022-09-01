palvras = ('armario', 'casa', 'jornal', 'maduro'
           , 'inativo', 'sempre'
           , 'estudar', 'te amo', 'alana')
for p in palvras:
    print(f'\nna palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
