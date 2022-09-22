try: #operação
    a = int(input('numerador: '))
    b = int(input('demominador: '))
    r = a/ b

except Exception as erro: #falhou
    print(f'Problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('tivemos problema com o tipos de dados que vc digitou')
except ZeroDivisionError:
    print('não é possivel dividir um numero por zero!')
except KeyboardInterrupt:
    print('o usuario preferiu não informar os dados')
else: # deu certo
    print(f'O resultado é {r:.1f}')
finally: # certo/falho
    print('volte sempre! Muito obrigado!')

