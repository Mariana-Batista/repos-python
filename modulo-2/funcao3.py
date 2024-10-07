"""
Retorno (return) de valores das funções
"""

#Print é uma função que exibe um valor na tela.

"""variavel = print('Mariana')
print(variavel)"""


'''
*args(empacotamento e desempacotamento)
'''

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# def soma (x, y):
#     return x + y

def soma(*args):
    total = 0
    
    for numero in args:
        print('Total', total, numero)
        total = total + numero
        print('Total', total)
    
soma(1, 2, 3, 4, 5, 6)


print("*********************************************")


def soma2(*args):
    total = 0
    
    for numero in args:
        total += numero
    
    print(total)
    
soma2(1, 2, 3, 4, 5, 6)
    
print("*********************************************")


def soma3(*args):
    total = 0
    
    for numero in args:
        total += numero
    return total
    
soma_1_2_3 = soma3(1, 2, 3)
print(soma_1_2_3)
    


