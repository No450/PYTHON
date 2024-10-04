"""
args - argumentos não nomeados 
* - *args (empacotamento e desempacotamento)
"""
#desempacotamento
x,y,*resto = 1,2,3,4,5,6
print(x,y,resto)
#por que isso acontece? - X = 1 , y = 2 , resto = [3,4] armazena em uma lista o restante 

def soma (x,*args):
    sum_number = 0 
    for sum_args in args:
        print(f"{sum_args}+{sum_number} = ",end="")
        sum_number += sum_args
        print(sum_number)
    print(f"A soma dos argumentos {args} = {sum_number}")

soma(1,3,4,5,6,)

