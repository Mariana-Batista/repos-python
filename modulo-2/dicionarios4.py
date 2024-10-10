# Lista de perguntas
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['10', '55', '25', '30'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['6', '5', '8', '9'],
        'Resposta': '5',
    }
]

# Função para verificar se a resposta do usuário está correta
def respostas_usuario(pergunta, escolha):
    if pergunta['Opções'][int(escolha)] == pergunta['Resposta']:
        print('Você acertou!\n')
    else:
        print(f'Você errou. A resposta correta é {pergunta["Resposta"]}.\n')

# Função para exibir a pergunta, opções e solicitar resposta
def mostrar_perguntas_e_opcoes(perguntas):
    for pergunta in perguntas:
        # Exibe a pergunta
        print('Pergunta:', pergunta['Pergunta'])
        
        # Exibe as opções da pergunta
        for i, opcao in enumerate(pergunta['Opções']):
            print(f'{i}: {opcao}')
        
        # Recebe a escolha do usuário
        escolha = input('Escolha o número da opção: ')
        print()
        
        # Verifica se a resposta está correta
        respostas_usuario(pergunta, escolha)

# Chama a função para exibir as perguntas e verificar as respostas
mostrar_perguntas_e_opcoes(perguntas)
        
        


