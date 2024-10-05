"""Calculadora com while"""

while True:
    numero_str = input('Digite um número: ')
    numero_str2 = input('Digite um número: ')
    operador_str = input('Digite o operador: [+][-][/][*] ')
    
    numero_validos = None
    
    numero_float1 = 0
    numero_float2 = 0
    
    try:
        numero_float1 = float(numero_str)
        numero_float2 = float(numero_str2)
        numero_validos = True

    except Exception:
       numero_validos = None
       
    if numero_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador_str not in operadores_permitidos: 
        print('O operador é inválido.')
        continue
    if len(operador_str) > 1: 
        print('Digite apenas um operador.')
        continue
################

    if operador_str == '+':
        print(f'{numero_float1} + {numero_float2} = ', numero_float1 + numero_float2)
    elif operador_str == '-':
        print(f'{numero_float1} - {numero_float2} = ', numero_float1 - numero_float2)
    elif operador_str == '/':  
       print(f'{numero_float1} / {numero_float2} = ', numero_float1 / numero_float2)
    elif operador_str == '*': 
        print(f'{numero_float1} * {numero_float2} = ', numero_float1 * numero_float2)
    else:
       print ('Error')
################
    
    sair = input('Você deseja sair? [s][n] ').lower().startswith('s')
    
    if sair is True:
        break
    
    