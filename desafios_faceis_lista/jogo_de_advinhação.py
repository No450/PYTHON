import random
palavra = ["Banana", "Maça", "Laranja", "Melancia", "Melão"]
palavra = random.choice(palavra)
palavra = palavra.upper()
letras_acertadas =''
cont = 0
while True:
    cont+=1
    letra_digitada = input("Digite uma letra: ")
    letra_digitada = letra_digitada.upper()
    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.")
        continue
    
    if cont == 5:
        print("Tente adivinhar")
        advinha_final = input("Digite a palavra:")
        advinha_final = advinha_final.upper()
        if advinha_final in palavra:
            print("Acertou")
            break
        else:
            print("Errou")
            continue

    if letra_digitada in palavra:
        letras_acertadas+= letra_digitada
    
    resultado = ''.join([letra if letra in letras_acertadas else '*' for letra in palavra])
    print(resultado)
    print("\n")
    if resultado == 'BANANA':
        print("Acertou")
        break
print(f"O numero de tentativas é {cont}")