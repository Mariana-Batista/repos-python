"""
Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

"""

"""def saudacao(msg):
    return msg

print(saudacao('Bom dia'))"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar()

s1 = criar_saudacao('Bom dia', 'Mariana')
s2 = criar_saudacao('Boa tarde', 'Apolo')
print(s1)
print(s2)

print('**********************************')

#Closure - Salva na memória antes de finalizar a função

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('Boa noite', 'Mariana')
s2 = criar_saudacao('Bom dia', 'Apolo')
print(s1())
print(s2())

print('**********************************')


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Mariana', 'Cristiane', 'Carlos']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))


print('**********************************')

numeros = [2, 3, 4]

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar=criar_multiplicador(2)
triplicar=criar_multiplicador(3)
quadruplicar=criar_multiplicador(4)

for numero in numeros:
    print(duplicar(numero))
    print(triplicar(numero))
    print(quadruplicar(numero))
