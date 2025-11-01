#Dissecando uma variavel

digitado = input("Digite algo: ")
print(f"O tipo primitivo desse valor é {type(digitado)}")
print(f"Só tem espaços? {digitado.isspace()}")
print(f"É um número? {digitado.isnumeric()}")
print(f"É alfabético? {digitado.isalpha()}")
print(f"É alpanúmerico? {digitado.isalnum()}")
print(f"Está em maiúscula? {digitado.isupper()}")
print(f"Está em minúscula? {digitado.islower()}")
print(f"Está capitalizada? {digitado.istitle()}")