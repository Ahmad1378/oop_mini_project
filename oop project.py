import random
rng = random.Random()
teams = []
for i in range(22):
    if i % 2 == 0:
        teams.append("A")
    else:
        teams.append("B")

class Person:
    def __init__( self , name):
        self.name = name

class Footbalist(Person):

    def select_team(self):
        rng.shuffle(teams)
        self.team = teams [0]
        teams.pop(0)

    def player_name(self):
        return self.name

    def team_name(self):
        return self.team

names_list = [ "Hossein" , "Maziar" , "Akbar" , "Nima" , "Mehdi" , "Farhad" , "Mohammad" , "Khashayar" ,
"Milad" , "Mostafa" , "Saeed" , "Amin" , "Pooya" , "Pooria" , "Ali" , "Reza" , "Behzad" , "Soheil" , "Behrooz" ,
"Shahrooz" , "Saman" , "Mohsen" ] 

names_dictionary = {}

for i in range(22):

    names_dictionary[names_list[i]] = Footbalist(names_list[i])
    names_dictionary[names_list[i]].select_team()

for i in range(22):
    print( names_dictionary[names_list[i]].player_name() , names_dictionary[names_list[i]].team_name() )