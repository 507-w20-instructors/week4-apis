
import requests
import json
import random

BASE_URL = "https://api.datamuse.com/words"


def random_word_from_word_list(word_list):
    index = random.randint(0, len(word_list) - 1)
    return word_list[index]["word"]


first_word = "red"
second_word = "blue"
third_word = "sweet"
fourth_word = "you"

'''
1. A word that rhymes with red
2. A word that has a similar meaning to blue
3. A word that is a synonym of sweet
4. A word that sounds like you
'''

params = {"rel_rhy":"red"}
response = requests.get(BASE_URL, params)
word_list = json.loads(response.text)
first_word = random_word_from_word_list(word_list)

# Get second word
params = {"ml":"blue"}
response = requests.get(BASE_URL, params)
word_list = json.loads(response.text)
second_word = random_word_from_word_list(word_list)

# Get third word
params = {"rel_syn":"sweet"}
response = requests.get(BASE_URL, params)
word_list = json.loads(response.text)
third_word = random_word_from_word_list(word_list)

# Get fourth word
params = {"sl":"you"}
response = requests.get(BASE_URL, params)
word_list = json.loads(response.text)
fourth_word = random_word_from_word_list(word_list)

poem = f'''
    Roses are {first_word}
    Violets are {second_word}
    Sugar is {third_word}
    And so are {fourth_word}
'''

print(poem)