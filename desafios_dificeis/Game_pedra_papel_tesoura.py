import time 
import random
#------------LISTAS---------------#
lista = ["PEDRA","PAPEL","TESOURA"]
vida  = ["❤️","❤️","❤️","❤️","❤️"]

conta_vitoria = 0 #conta a quantidade de vitorias
conta_derrota = 0 #conta a quantidade de derrotas
conta_empate  = 0 #conta a quantidade de empates 
i = 0 #conta as tentativas
j = 0 #condicao para a revanche 
pergunta_revanche = {} 

while pergunta_revanche != "N":
    i+=1 #incrementa +1 ao i
    valor_aleatorio = random.choice(lista) #Gera aleatoriamente a lista ["PEDRA","PAPEL","TESOURA"]
    print("="*10,"JOGO DE PEDRA PAPEL TESOURA","="*10)
    jogada_usuario = input("Faca a sua Jogada:") #ler a opcao do usuario
    jogada_usuario = jogada_usuario.upper() 
    print(f"{i} tentativa") #mostrar o numero de tentativas incrementadas 
    print(f"Escolhi: {valor_aleatorio}") #mostrar valor gerado aleatoriamente 
    print("Vidas: ",end="")
    for mostra_vida in range(len(vida)):
        print(vida[mostra_vida],end="")
    print("\n")
    
    a = jogada_usuario == 'PAPEL'   and valor_aleatorio == 'PEDRA' 
    b = jogada_usuario == 'TESOURA' and valor_aleatorio == 'PAPEL' 
    c = jogada_usuario == 'PEDRA'   and valor_aleatorio == 'TESOURA' 
    
    if jogada_usuario == valor_aleatorio:
        print(">"*20," EMPATE ","<"*20,"\n")
        conta_empate+=1

    elif (a or b or c):
        print(">"*20," VENCEU ","<"*20,"\n")
        conta_vitoria+=1

    elif (jogada_usuario != "PEDRA" and jogada_usuario != "PAPEL" and jogada_usuario != "TESOURA"):
        print("Valor invalido")
        break
    else:
        print(">"*20," PERDEU ","<"*20,"\n")
          
        remove = vida.pop()
        print("Vida Agora: ",end="")
        for remove_vida in range(len(vida)):
            print(vida[remove_vida],end="")
        conta_derrota+=1
        print("\n")
        for j in range(3,i,3):
            pergunta_revanche = input("Deseja ter uma revanche? S/N: ")
            pergunta_revanche = pergunta_revanche.upper()  
        if vida == ['']:
            print("GAME OVER")
print(f"Eu ganhei {conta_derrota} vezes e voce ganhou de mim {conta_vitoria} vezes e teve {conta_empate} empates")
