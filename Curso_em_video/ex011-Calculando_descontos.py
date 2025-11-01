Preco = float(input("Qual é o preço do produto? R$"))
desconto = Preco - (Preco * 0.05)
print(f"O produto que custava R${Preco}, na promoção com descontos de 5% vai custar R${desconto:.2f}")
