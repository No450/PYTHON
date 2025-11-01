dolar_real = 5.37 #1 dolar equivale a 5,37
carteira = float(input("Digite um valor em real: "))
valor_convertido = carteira/dolar_real
print(f"O valor de R${carteira} em dolar é U${valor_convertido:.2f}")
