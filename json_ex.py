import json

json_str = '''
    [{"a":"apple", "b": "banana"},{"a":"apricot", "b":"blueberry"}]
    '''

fruit_dict_list = json.loads(json_str)

print(type(json_str))
print(type(fruit_dict_list))
print(type(fruit_dict_list[0]))
print(fruit_dict_list[0]["b"])



the_dict = {'g': 'grape', 'p': 'plum', 'n': 'nectarine'}
dict_json_str = json.dumps(the_dict)
print(type(dict_json_str))
print(dict_json_str)