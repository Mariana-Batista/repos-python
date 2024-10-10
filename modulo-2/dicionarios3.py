#Métodos úteis

pessoa = {
    'nome' : 'Apolo',
    'sobrenome' : 'Solaris',
    'idade' : 24,
    'altura' : 1.80,
    'enderecos': [
        {'rua': 'Sol', 'número': 123},
        {'rua': 'Olimpo', 'número': 101},
    ],
}

#print(len(pessoa))

#print(pessoa.keys())

#print(list(pessoa.keys()))

#print(list(pessoa.values()))

#print(pessoa.items())

# pessoa.setdefault('ocupação', 'Deus do sol')
# print(pessoa['ocupação'])

# Cópia valores imutáveis
# pessoa_2 = pessoa.copy() #'Cópia rasa'
# pessoa_2 ['nome'] = 'Ares'
# pessoa_2 ['sobrenome'] = 'Guerreiro'
# print(pessoa_2)

# import copy

# pessoa_2 = copy.deepcopy(pessoa) #'Cópia profunda'
# pessoa_2 ['nome'] = 'Ares'
# pessoa_2 ['sobrenome'] = 'Guerreiro'
# print(pessoa_2)

#print(pessoa.get('nome'))

