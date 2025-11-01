numero = int(input("Me diga um número qualquer: "))

if numero % 2 == 0:
    print(f"O número {numero} é \33[1;31mPAR\33[0m")
else:
    print(f"O número {numero} é \033[1;33mIMPAR\33[0m")
