def notas(*notas, situação=False):
    """
    -> função para analisar a situação de varios alunos.
    :param notas: notas para o armazenamento e calculo(aceita varias).
    :param situação: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionario com varaias informações.
    """
    dic = dict()
    soma = 0
    for c in notas:
        soma += c
    min(notas)
    dic['quantidade de notas'] = len(notas)
    dic['maior nota'] = max(notas)
    dic['menor nota'] = min(notas)
    dic['media da turma'] = soma / len(notas)
    if situação:
        if dic['media da turma'] >= 7:
            dic['situação'] = 'BOA'
        elif dic['media da turma'] >= 5:
            dic['situação'] = 'razoavel'
        else:
            dic['situação'] = 'Ruim'
    return dic


resp = notas(6, 6, 6, 6, 6, 6, 7, 10, 11, 9,  situação=True)
print(resp)


#modo curso em video

def note(*n, situ=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if situ:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'Razoavel'
        else:
            r['situação'] = 'ruim'
    return r


resp = note(5.5, 2.5, 1.5, situ=True)
print(resp)
