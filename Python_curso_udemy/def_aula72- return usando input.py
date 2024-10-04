"""
print é uma função que foi criado com intuito de jogar valores na saida do sistema (executar uma ação /Mostrar algo na tela)
Print por padrão retorna None

variavel = print("Luiz")
print(variavel is None)
-------------------------
Print (exibi algo na tela | nao faz mais nada )
return (retorna dentro da funcao e metodos) - O retorno Para tudo e retorna o que esta pedindo 
-----------------------------------------------------------------------------------------------
#variavel = soma(1,2)
#variavel = int("1") #Parece uma funcao/ não é uma função / salvando o valor em uma variavel
#print(variavel)
"""

def soma(x,y):
    return(x + y)

soma1 = soma(2,2)
soma2 = soma(3,4)
print(soma1+soma2)


def year_18(a):
    if a >= 18: 
        return "Maior de idade" 
    return "Menor de idade"


idade = int(input("Digite sua idade: "))
print(year_18(idade))
