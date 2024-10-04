"""
Closure e funções que retornam outras funções 
salutation = saudação 
para o python retornar o valor da função ele vai precisar salavar na memoria e quando executar ele pega o valor da memoria 
e te entrega 

"""

def criar_saudacao (saudacao):
    def saudar (nome):
        return f'{saudacao}, {nome}!'
    return saudar
    
Falar_bomdia = criar_saudacao("Bom dia")
Falar_boaNoite = criar_saudacao("Boa noite")

for nome in ["Maria","Joana","Luiz"]:
    print(Falar_bomdia(nome))
    print(Falar_boaNoite(nome))
