"""
print(User.values())
print(User.keys())
print(User.items())


User = dict()
print(User, type(User))

"""

User = {
    "Player": "Noam_986",
    "year": 22,
    "Class_person": "Mage",
    "Atribute": "Fire",
    "life": 145,
    "Level": 30,
    "Status_life": True 
}
print(User["life"],"\n")
#pode ser feito assim ou :
for i,j in User.items():
    print(f"{i} : {j}")
#pode ser feito assim 
print("\n")
for chave in User: 
    print(chave,User[chave])