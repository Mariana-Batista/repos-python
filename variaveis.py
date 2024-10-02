"""
Constante = 'Variáveis' que não vão mudar!

Quando é uma váriavel que não vai mudar ao longo do programa, usar letras maiusculas! Isso indica que não deve ser alterado.

Muitas condições dentro de um if NÃO é uma boa prática.
"""

velocidade = 62 #velocidade atual do carro
local_carro = 100 #Km em que o carro está na estrada

RADAR_1 = 60 #velocidade máxima do radar 1
LOCAL_1 = 100 #local onde o radar está
RADAR_RANGE = 1 #distância onde o radar pega

velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_passou_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) 
carro_multado_radar1 = carro_passou_radar1 and velocidade_carro_passou_radar1 > RADAR_1

if velocidade_carro_passou_radar1:
    print('Velocidade que o carro passou do radar 1')
    
if carro_passou_radar1:
    print('Carro passou radar 1')
    
if carro_multado_radar1:    
    print ('Carro multado em radar 1') 