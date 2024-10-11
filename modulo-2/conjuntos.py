#Set (classe) em Python, são tipos de dados que são mutáveis, mas aceitam apenas tipos imutáveis como valor interno.
#Eficientes para remover valores duplicados de iteráveis

s1 = set('Mariana') #Não garante a ordem dos elementos
print(s1, type(s1))

print()

s2 = {'Mariana', 1, 2, 3} #Set com dados
print(s2)

print()

s3 = {1, 1, 5, 4, 4, 4, 6}
print(s3)

print()

#Removendo valores duplicados de uma lista, usando o set
lista_1 = [2, 2, 5, 5, 5, 6, 6, 7, 8, 9, 9]
s4 = set(lista_1)
lista_nova = list(s4)
print(lista_nova)

print()
"""Não tem índexes - TypeError: 'set' object is not subscriptable
s5 = {1, 2, 3}
print(s5[1])""" 

s6 = {2, 4, 6}
print(1 in s6) #False
print(2 not in s6)
print(2 in s6) #True