te = input('digite algo: ')
x = str(type(te))
x2 = str(te.isalpha())
x3 = str(te.isspace())
x4 = str(te.isnumeric())
print('o tipo primitivo desse valor é{}.        '
      'é alfabetico? {}.        '
      'é preenchido por espaços?{}.     '
      'é numerico?{}.   '.format(x, x2, x3, x4))
