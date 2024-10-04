"""
#Method useful of the dicionary and python - metodos uteis dos dicionarios em python 
#len - how many key - quantas chaves 
#keys - iterate with of keys - iteravel com a chaves 
#Values - iterate with of values - iteravel com valores 
#items - iterate with keys and values - iteravel com chaves e valores 
#setdefault - add values to keys if she not exist - adicionar valores em chave se ela nao existir
#copy - return a copy shallow - retorna uma copia rasa 
#get - get a key - Obtem uma chave 
#pop - erase a item with the key especific (del) - apaga um item com a chave especifica 
#popitem - erase the final item add
#update - update a dicinary with other - atualiza o dicionario com outro 

#print(len(person))
print(person.items())
print(person.values())
print(person.keys())

for i in person:
    print(i)
    
for chave, valor in person.items():
    print(chave,valor)    
    
"""
person = {
    "first_name": "Noam Willyan",
    "last_name": "Miranda3",
    #"age" : 900
}

person.setdefault('age',0)
print(person['age'])
