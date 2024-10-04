#copia um elemento permitindo altera-lo e fazer copias dele 
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1,4,5],
}
d2 = d1.copy() #d2 points for the dicionary that é d1 - aponta para o mesmo dicionario que d1

d2['c1'] = 1000
d2['l1'][1] = 999 #todos os valores serão alterados (cópia rasa)
print(d1)
print(d2)

