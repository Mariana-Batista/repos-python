'''
Introdução ao try/except
Try - tentar executar o código
Except - ocorreu um erro ao tentar executar
'''

numero_str = input('Vou dobrar o número que você digitar: ')

"""if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
else:
    print('Você não digitou um número!')"""
    
"""O if não evita erros, diferente do try/except"""

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número!')
