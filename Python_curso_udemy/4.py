p1 = {
    'Nome':'Luiz',
    'Sobrenome': 'Otavio',
    'idade': 18
}
#print(p1.get('Nome','Não existe'))
#remove_ultimo = p1.popitem()
#sobrenome = p1.pop("Sobrenome")
#p1.update({
#    'Nome': "Novo valor",
#    'estado': "MA",
#})

p1.update(nome = 'Novo valor', idade = 24, )
print(p1)