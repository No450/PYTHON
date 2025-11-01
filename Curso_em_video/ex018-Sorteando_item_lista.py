#Sorteando valores
import random
alunos = []

for cont in range(0,5):
    alunos.append(input("Digite o nome do aluno: "))
escolha = random.choice(alunos)
print(f"O aluno escolhido foi: {escolha}")
