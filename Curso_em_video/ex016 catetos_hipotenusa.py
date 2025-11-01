import math
cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
outra_hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")
print(f"Outro jeito de ter a hipotenusa é {math.sqrt(outra_hipotenusa):.2f}")
