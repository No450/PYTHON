
def saudacao (nome1):
    for percorrer in nome1: 
        print (f"Prazer em te conhecer {percorrer}!")
    

def criar_saudacao(*s1):
        return saudacao(s1)
    
    
s1 = criar_saudacao("Maria","Joao","heitor")
