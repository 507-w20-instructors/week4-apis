
import requests
import json

baseurl = "https://api.datamuse.com/words"
params_dict = {'rel_rhy':'blue'}
response = requests.get(baseurl, params_dict)
word_list = json.loads(response.text)
print(word_list[0]["word"]) # just get the first "word"