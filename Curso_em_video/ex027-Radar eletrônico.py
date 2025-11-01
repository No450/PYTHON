velocidade_carro = int(input("Qual a velocidade do carro atual? "))
if velocidade_carro > 80:
    multa = (velocidade_carro - 80)*7
    print("\033[1;31mMULTADO! Você excedeu o limite permitido que é de 80km/h\033[0m")
    print(f"Você deve pagar uma multa de R${multa:.2f}!")
    print("\033[1;33m Tenha um bom dia! Dirija com segurança! \033[0m")
else:
    print("\033[1;33m Tenha um bom dia! Dirija com segurança! \033[0m")
