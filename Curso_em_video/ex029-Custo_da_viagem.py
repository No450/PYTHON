#Calcular o preço da passagem. cobrando 0.50 por km para viagens de até 200km
#e 0,45 para viagens mais longas

distancia = float(input("Qual é a distância da sua viagem? "))
print(f"Você está prestes a começar uma viagem de {distancia}km")

if distancia <= 200:
    preco_passagem = (distancia * 0.50)
    print(f"E o preço da sua passagem será de R${preco_passagem:.2f}")
else:
    preco_passagem = (distancia * 0.45)
    print(f"E o preço da sua passagem será de R${preco_passagem:.2f}")

