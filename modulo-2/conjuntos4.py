#Exemplo de uso do set

"""
O usuário escolhe uma letra e a letra é salva em um conjunto set.
A letra misteriosa é escolhida aleatoriamente pelo programa e fica salva na varivável letra_misteriosa.
O programa faz um comparação entre a letra escolhida e a letra_misteriosa.
Se o usuário acertar a letra, o programa imprime na tela uma parabenização.
"""

import random
import string

# letras = set()

# while True:
#     letra = input('Digite uma letra do alfabeto: ')
#     letras.add(letra.lower())
    
#     if 'm' in letras:        
        
#         print('Parabéns! Acertou a letra')
#         break
    
#     print(letras)
    

print('Jogo Letra Misteriosa')

letras_escolhidas = set()  # Conjunto para armazenar as letras já escolhidas

letra_misteriosa = random.choice(string.ascii_lowercase)  # Gera uma letra aleatória minúscula
#print(letra_misteriosa)  # Você pode descomentar essa linha para fins de depuração, caso queira ver a letra misteriosa.

while True:
    letra = input('Digite uma letra do alfabeto: ').lower()  # Converte a letra digitada para minúscula
    letras_escolhidas.add(letra)  # Adiciona a letra ao conjunto
    
    if letra == letra_misteriosa:  # Verifica se a letra digitada é a letra misteriosa
        print('Parabéns! Acertou a letra')
        break
    
    print(f'Letras já escolhidas: {letras_escolhidas}')


