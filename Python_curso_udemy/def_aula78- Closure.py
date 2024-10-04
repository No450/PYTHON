"""
Closure e funções que retornam outras funções 
salutation = saudação 
para o python retornar o valor da função ele vai precisar salavar na memoria e quando executar ele pega o valor da memoria 
e te entrega 

"""

def criar_saudacao (saudacao, nome):
    def saudar ():
        return f'{saudacao}, {nome}!'
    return saudar
    
s1 = criar_saudacao("Bom dia", "Luiz")
s2 = criar_saudacao("Boa noite", "Maria")

print(s1())
print(s2())

