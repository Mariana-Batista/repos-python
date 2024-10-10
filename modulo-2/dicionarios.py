#Tipo Dict - Estrutura de dados - par de chave e valor

#Dados retornados como um dicionário facilita o uso para finalidades como gravação em banco de dados, API, etc.

pessoa = {
    'nome' : 'Apolo',
    'sobrenome' : 'Solaris',
    'idade' : 24,
    'altura' : 1.80,
    'enderecos': [
        {'rua': 'Solar', 'número': 123},
        {'rua': 'Olimpo', 'número': 101},
    ],
}

pessoa_2 = dict(nome = 'Zeus', sobrenome = 'Gregoriano', idade = 53, altura = 2.00, enderecos = {'rua': 'Olimpo', 'número': 100})

print(pessoa, type(pessoa))
print(pessoa_2, type(pessoa_2))
print(pessoa['nome'])









