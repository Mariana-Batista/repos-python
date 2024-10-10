#Chaves dinâmicas

pessoa = {}

chave = 'Nome'

pessoa[chave] = 'Mariana'
pessoa ['Sobrenome'] = 'Batista'

print(pessoa[chave])

pessoa[chave] = 'Cristiane'

del pessoa['Sobrenome']
print(pessoa)
print(pessoa['Nome'])

#If não para exceção.
#ex.

if pessoa.get('Sobrenome') is None:
    print('A chave não existe')
else:
    print(pessoa['Sobrenome'])
    