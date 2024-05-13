"""
Append - adiciona um item ao final
insert - adiciona no final ou no indice escolhido
pop - remove no final ou no insdice escolido 
del - apaga indice
clear - limpa a lista
extend - estende a lista
+ - -concatena a lista
"""
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[3] #deleta o indice 40
del lista[3] #deleta o indice 1233
lista.insert(0, 'Luiz') #vai inserir no indice 0 o valor 'Luiz'
print(lista)
