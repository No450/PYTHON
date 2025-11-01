import random

lista = []

while True:
    lista.append(input("Digite o nome do aluno: "))
    pergunta = str(input("Deseja continuar[S/N]: "))
    if pergunta == "N":
        break
random.shuffle(lista)

print(lista)
