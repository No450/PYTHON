import os
#calculadora usando em funções (def)

def menu():
    print("=" * 22)
    print("[1] Adição")
    print("[2] Subtração")
    print("[3] Multiplicação")
    print("[4] Divisão")
    print("[5] Sair")
    print("=" * 22)
    return int(input("Digite sua escolha: "))

def ler_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    return num1, num2

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def main():
    escolha = 0
    while escolha != 5:
        escolha = menu()
        if escolha == 5:
            print("Programa finalizado com sucesso!")
            break

        num1, num2 = ler_numeros()

        if escolha == 1:
            print(f"O valor da soma é {adicao(num1, num2)}")
        elif escolha == 2:
            print(f"O valor da subtração é {subtracao(num1, num2)}")
        elif escolha == 3:
            print(f"O valor da multiplicação é {multiplicacao(num1, num2)}")
        elif escolha == 4:
            print(f"O valor da divisão é {divisao(num1, num2)}")
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()