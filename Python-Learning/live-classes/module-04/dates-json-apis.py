# import datetime

# print(datetime.datetime.now())


# from datetime import datetime, date, time

# this_moment = datetime.now()

# print(this_moment)
# print(this_moment.second)

# birth = datetime(2025, 5, 2, 8, 3, 15)
# print(birth)

# a = date.today()
# print(a)


# from datetime import datetime, timedelta

# print(type(datetime.now()))

# ekhon = datetime.now()
# meeting = datetime(2026, 10, 11, 19)

# print(ekhon)
# print(meeting)

# diff = meeting - ekhon

# print(diff)
# print(type(diff))


# print(datetime.now() + timedelta(days=5))


# from datetime import datetime

# ekhon = datetime.now()

# print(ekhon.strftime("%B %d, %Y"))  # September 28, 2026


# import json

# data = {
#     "name": "Zayed",
#     "class": 7,
#     "roll": 99,
#     "isPassed": False,
# }
# data = ["Apple", "Banana", {"name": "Jackfruit"}]

# # data_in_text = str(data)
# # print(data_in_text)

# print(data)
# print(type(data))

# res = json.dumps(data)
# print(res)
# print(type(res))

# with open("data.json", "w") as f:
#     # f.write(str(data)) # WRONG
#     f.write(res)

# print(res)
# print(res[2])

# import json

# with open("data.json", "r") as f:
#     content = f.read()
#     print(content)
#     print(type(content))

#     data = json.loads(content)
#     print(data)
#     print(type(data))
#     print(data[0])


# import requests

# a = 5

# URL = "https://dummyjson.com/products"

# res = requests.get(URL)

# print(res)
# # print(res.text)
# print(type(res.text))
# print(type(res.json()))

# print(res.text["products"])

# import json

# data = json.loads(res.text)

# print(type(data))
# print(data["products"][2]["title"])
