#args they are tuple, where i can to speend values ilimited 
#use the sun / use o sum para poder somar os valores ex:
#print(sum((1,2,3,4,5,6)))

def sum_(*args):
    print(args)
    total = 0 
    for sum_args in args: 
        total+= sum_args
    return total
    
sum_values_a = sum_(1,3,6)
print(f">>{sum_values_a} \n")

sum_values_b = sum_(8,3,4)
print(f">>{sum_values_b} \n")

number= 1,4,5,6,7,8,3,9
other_sum = sum_(*number)
print(f">>{other_sum}\n")

print(*number)
print(f">>{sum(number)}") #desempacotando 