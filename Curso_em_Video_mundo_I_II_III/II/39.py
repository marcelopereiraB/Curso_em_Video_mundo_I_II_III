from datetime import date

cal = date.today().year
nas = int(input('qual seu ano de nascimento? '))
idade = cal - nas
if idade < 18:
    print('voce ainda não atingiu a idade adequada')
    print(f'seu alistamento sera em {(18 - idade) +cal}')
elif idade == 18:
    print('chegou a hr de se alistar, procure a justa militar assim que possivel')
elif idade >= 19:
    print(f'ainda não se alistou? esta com um atraso de {idade - 18} anos')
