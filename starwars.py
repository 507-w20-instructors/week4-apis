# starwars

import requests

BASE_URL = "http://swapi.co/api"
BASE_URL_PEOPLE = BASE_URL + "/people"


class Character():

    
    def __init__(self, 
                 name, 
                 species):

        self.name = name
        self.species = species


    def info(self):
        return self.name + ' is a ' + self.species


class Human(Character):


    def __init__(self, 
                 name,
                 hair_color):
        super().__init__(name,"human")
        self.hair_color = hair_color

    def info(self):
        return super().info() + " with " + self.hair_color +  " hair"



##### init objects by hand
luke = Human("Luke Skywalker",
                 "blonde")

leia = Human("Leia Organa",
                 "brown")

c3po = Character("C3PO",
                 "droid")

people = [luke, leia, c3po]

for p in people:
    print(p.info())


##### init objects from API/JSON
# r = requests.get(BASE_URL_PEOPLE)
# people_list = r.json()['results']
# next = r.json()['next']

# print(next)
# for p in people_list:
#     print(p["name"])

