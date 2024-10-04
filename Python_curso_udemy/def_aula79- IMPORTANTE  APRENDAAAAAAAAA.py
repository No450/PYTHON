def criar_multiplicador(multiplicador):
    def multi (number):
        return number * multiplicador
    return multi

num2 = int(input("Digite outro numero: "))
dobro = criar_multiplicador(num2)
triplo = criar_multiplicador(num2)
quadruplo = criar_multiplicador(num2)

print(dobro(2))
print(triplo(3))
print(quadruplo(4))
