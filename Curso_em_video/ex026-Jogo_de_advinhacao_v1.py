import time
from random import randint
from time import sleep

print("-="*27)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-="*27)
robo = randint(0, 5)
numero = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
time.sleep(2)

if numero == robo:
    print("Você ganhou! Parabéns")
elif numero != robo:
    print(f"GANHEI Eu pensei no número {robo} e não no {numero}!")
else:
    print("Valor invalido")
