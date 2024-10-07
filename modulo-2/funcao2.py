"""
Escopo global
"""
x = "O x foi definido em escopo global, podendo ser acessado pela função e fora da função"

def escopo_global():
    print(x)

escopo_global()


"""
Escopo local
"""
print("**************")

def escopo_local ():
    y = "O y foi definido em escopo local, ou seja, dentro da função"
    print(y)

escopo_local()


print("***************")

def funcao_com_outra_funcao():
    x = "Essa variável apenas poderá ser usada dentro desta função"
    
    def outra_funcao():
        x = "Esse x somente poderá ser usado dentro da função 'outra_funcao'"
        y = "O mesmo acontece com esse y, quanto mais interno, o escopo é mais fechado"
        print(x, y)
        
    outra_funcao()
    print(x)
    
print(x)
funcao_com_outra_funcao()
print(x)    