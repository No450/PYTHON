Valor_1 = int(input('Primeiro valor: '))
Valor_2 = int(input('Segundo valor: '))
Valor_3 = int(input('Terceiro valor: '))

menor = Valor_1
maior = Valor_1

if Valor_2 < Valor_1 and Valor_2 < Valor_3:
    menor = Valor_2

if Valor_3 < Valor_1 and Valor_3 < Valor_2:
    menor = Valor_3

if Valor_1 > Valor_3 and Valor_1 > Valor_2:
    maior = Valor_2

if Valor_3 > Valor_1 and Valor_3 > Valor_2:
    menor = Valor_3


print("O menor valor digitado foi {}".format(menor))
print("O maior valor digitado foi {}".format(maior))



