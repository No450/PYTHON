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
#p1.update(nome = 'Novo valor', idade = 24, )

tupla = (('Nome','novo valor'), ('idade',30))
lista = [['Nome','Matheus'], ['idade',40]]
p1.update(tupla)
print(p1)
p1.update(lista)
print(p1)