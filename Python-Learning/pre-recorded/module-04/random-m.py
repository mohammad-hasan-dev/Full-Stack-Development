import random

# help(random)
# print(dir(random))
# print(random.__doc__)
# print(random.random())
# print(random.uniform(5,10))
# print(random.randrange(1,1000))
# fruits=['apple','banana','cherry']
# print(random.choice(fruits))
# random.shuffle(fruits)
# print(fruits)
def gn_pin():
    return random.randint(1000,9999)
print(f"Your 4 digit pin {gn_pin()}")

