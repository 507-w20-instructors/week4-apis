

import requests

BASE_URL = "http://swapi.co/api/people" # only interested in people

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]
print(people_list[3]["name"], people_list[3]["eye_color"])
for p in people_list:
    print(p["name"])
exit()



class Character:

    def __init__(self, nm, sp):
        self.name = nm
        self.species = sp

    def info(self):
        return self.name + " is a " + self.species

luke = Character("Luke Skywalker", "Human")
c3po = Character("C3PO", "Droid")

print(luke.info())
print(c3po.info())