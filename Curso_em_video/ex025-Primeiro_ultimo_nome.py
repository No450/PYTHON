# use o split, fatiamento e strip
nome = str(input('Digite seu nome completo: ')).upper().strip()
print("Prazer em te conhecer!")
nome = nome.split()
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[len(nome)-1]}")

