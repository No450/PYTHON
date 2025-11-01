#escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
#R$60 por dia e R$0,15 por km rodado. 

dias_alugados = int(input("Quantos dias alugados? "))
km_rodados = int(input("Quantos Km rodados? "))

custo_carro_dia = 60 * 8
km_rodados = km_rodados * 0.15
print(f"O total a pagar é de R${km_rodados+custo_carro_dia}")

