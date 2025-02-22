import json

person = { "name":"sushil", "age": 25, "city":"New Delhi", "has children":False, "titles": ["engineer" , "programmer"] }

personJSON = json.dumps(person, indent=3 ,sort_keys= True)
# print(personJSON)


