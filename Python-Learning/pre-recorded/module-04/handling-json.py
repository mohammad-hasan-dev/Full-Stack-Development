import json
# data = {
#     'name': "Rahim",
#     'age': 30,
#     'is_logged_in': True,
# }

# #serialixation : pyhton -> json
# json_str = json.dumps(data, indent=4)
# print(json_str)

#deserialixation : pyhton -> json

data = '{ "name": "Rahim","age": 30,"is_logged_in": true}'
python_dict = json.loads(data)
print(python_dict, type(python_dict))