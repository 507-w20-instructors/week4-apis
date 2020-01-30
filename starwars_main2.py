import requests
import starwars_character2

#### Fetching Character data from swapi.co
BASE_URL = "http://swapi.co/api/people" # only interested in people

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]
characters = []
for p in people_list:
    characters.append(starwars_character2.Character(character_data=p))

for c in characters:
    print(c.info())
