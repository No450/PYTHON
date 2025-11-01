num = int(input("Digite um número: "))

contador = 1
print("="*12)
while (contador != 11):
    print(f"{num} X {contador} = {num * contador}")
    contador = contador + 1
print("="*12)