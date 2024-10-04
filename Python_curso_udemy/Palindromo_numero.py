def encontrar_palindromos(numero_inicial, numero_final):
    for i in range (numero_inicial,numero_final):
        converte_numero_str = str(i) # '12' 
        inverte_numero = converte_numero_str[::-1] #'21' 
        converte_numero_int = int(inverte_numero)#21
        converte = int(i)#12
        
        if (converte_numero_int == converte):
            print(converte,end=" ")
    
numero_inicial = int(input("Inicio: "))
numero_final = int (input("Final: "))
print("-"*6," Palindromos ","-"*6) 
encontrar_palindromos(numero_inicial,numero_final)