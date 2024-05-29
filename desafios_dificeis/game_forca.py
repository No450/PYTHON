import random

forca = ["BANANA", "MAÇA", "PERA", "MELANCIA", "ESTANDE", "ONITORRINCO", "LEÂO-MARINHO", "LOUVA-DEUS"]
vida = ["💀","💀","💀","💀","💀"]
Robô_advinha = random.choice(forca)
# condição fazer -> realize um numero de tentativas sem fazer relação com a vida ou seja se chegar a vida a 1 ele deve chutar se se errar morre 
def linha ():
    print("="*22)

linha()
print("|    JOGO DA FORCA   |")
linha()

# imprimir os _ corresponndentes a escolha do robô
ler_tamanho = len(Robô_advinha) #se for PERA SERá 4
estado_atual = ["_"] * ler_tamanho # _ _ _ _

def exibir_estado_atual():
    print(" ".join(estado_atual))
exibir_estado_atual()

cont =  len(vida)
# ------------------COMEÇO-------------------------
for tentativa in range(len(vida)): # for de 4
    cont-=1
    print("\n")
    escolha_usuario = input("Digite uma letra: ").upper() # colocara o valor digitado em maiusculo 

    if cont == 1:
        exibir_estado_atual()
        print("\n")
        tente_advinhar = input("Tente adivinhar: ")
        if tente_advinhar == Robô_advinha:
            linha()
            print("Você acertou!")
            linha()
        else:
            linha()
            print("Voce morreu")
            linha()
            break

    if len(escolha_usuario) > 1: 
        print("ERROR: DIGITE APENAS UMA LETRA")
    elif len(escolha_usuario) == 1: # Se a letra ex: "A" 
        if escolha_usuario in Robô_advinha: # se a escolha do usuario estiver em robo advinha
            for index,valor in enumerate(Robô_advinha): #capturar o indice e depois o valor
                if valor == escolha_usuario: #se a letra do enumerate ex: se "A" for igual a escolha do usuario (A)
                    estado_atual[index] = escolha_usuario
            exibir_estado_atual()
            linha()
            print("Parabens você ganhou!!")
            linha()
        else:
            vida.pop()
            exibir_estado_atual()
            linha()
            print("Letra incorreta ")
            print("Vidas restantes: " +  " ".join(vida))
            linha()
