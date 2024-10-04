def multi_args(*args):
    total = 1 
    for multi in args:
        total*=multi 
    return total
    
variable_multiplicate = multi_args(4,6,6,3,5)
print(variable_multiplicate)


def even_or_odd (*args): #par ou impar
    for traverser in args: #percorrer o args
        result = traverser % 2 == 0
        if result: 
            print(f"Pares são: {traverser}")
        if not result:
            print(f"Impares são: {traverser}")
even_or_odd(5,6,4,3,2)

def par_impar (values):
        if values % 2 == 0:
            return "O numero é par"
        return "O numero é impar"
    
numero = int(input("Digite um numero: "))
print(par_impar(numero))
