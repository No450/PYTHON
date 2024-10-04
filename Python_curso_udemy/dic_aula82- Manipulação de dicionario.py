"""
print(User.values())
print(User.keys())
print(User.items())


User = dict()
print(User, type(User))


"""
pessoa = {}

chave = "nome"
pessoa[chave] = "luiz otavio"
pessoa["Sobrenome"] = "miranda"

print(pessoa[chave]) #values 
pessoa[chave] = "Maria"

del pessoa["Sobrenome"]
print(pessoa)
print(pessoa["nome"])

#print(pessoa.get("Sobrenome")) por padrao retorna None 
if pessoa.get("Sobrenome")is not None:
    print(pessoa['Sobrenome'])
else:
    print("Não existe")

    