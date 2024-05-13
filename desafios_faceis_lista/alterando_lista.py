"""
Tipo list - Mutável 
Suporta vários valores de qualquer tipo conhecimento reutilizado
método úteis:
    append, insert, pop, del, clear, extend, + 
    create read update Delete(CRUD)
    criar, ler , alterar, apagar = lista[i] 
    A lista pode ser interessante para retirar e adicionar no final dele
"""
lista = [10, 20, 30, 40]
lista[2] = 300
del lista[2]
lista.append("A") 
lista.pop() #remove o A e depois imprime adicionando o B /pega o ultimo valoe
lista.append("B") 
ultimo_valor = lista.pop(1)# se deixar o 1 ele removera o 1 indice , se deixar ele vazio removerá o ultimo indice
print(f"{lista}'Removido:'{ultimo_valor}")
print(lista)
print(lista[2])
