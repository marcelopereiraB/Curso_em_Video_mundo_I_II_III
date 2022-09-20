#como add elementos em um tupla com função e sem
tu = (int(input('insira um numero: ')), int(input('insita um numero: ')), int(input('insira um numero: ')), int(input('digite um numero: ')))
print(tu)

def funcao():
    return int(input('insira um numero: '))


tupla = (funcao(), funcao(), funcao(), funcao())
print(tupla.count(10))
print(tupla)
