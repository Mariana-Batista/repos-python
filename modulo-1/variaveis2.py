"""
Valor na memória

Flag (Bandeira) = Marca um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade"""

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

"""Local registrado na memória:
140727729229024
140727729229024


Quando as variáveis forem chamadas, retornaram o mesmo valor na memória,
porque apesar de serem duas váriaveis, receberam o mesmo valor (a)
"""

condicao = False

if condicao:
    
    print('Faça algo')
else:
    print('Não faça algo')