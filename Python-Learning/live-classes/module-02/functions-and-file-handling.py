# ==========================================
# multiple list indexing
# ==========================================

# ---->1st example
# items= [[1,2,3,4],[5,6,7,[8,9,10]]]
# a= items[0]
# b=items[1]
# print(a,b)

# ---->2nd example
# items= [[1,2,5],[2,[5,7,[2,4,6]]]]

# print(items[1][1][2][2])


# ==========================================
# set operations
# ==========================================

# num1={1,2,3,4,5}
# num2={4,5,6,7}
# print("union: ",num1 | num2) #union
# print("union: " ,num1.union(num2)) #union

# print("intersection : ",num1 & num2) #intersection 
# print("intersection : ",num1.intersection(num2)) #intersection 


# print("difference : ",num1 - num2) #difference 
# print("difference : ",num1.difference(num2)) #difference 


# ==========================================
# dictionary
# ==========================================

# student={
# "name":"kashem",
# "platform": "ostad",
# "course": "Data Science",
# "batch": 38,
# "is_valid": True
# }
# print(type(student))
# print(student["name"])
# print(type(student["batch"]))
# print(type(student["is_valid"]))
# print(student.items())
# print(student.keys())
# print(student.values())

# ==========================================
# dictionary 2nd example (items addressing)
# ==========================================

# student= {
# "name":"kashem",
# "platform": "ostad",
# "course": "Data Science",
# "batch": 38,
# "is_valid": True
# }

# for i in student.items():
#     print(i[0],"-" ,i [1])


# ==========================================
# foor loop
# ==========================================


# stations= ["motijheel","shochibaloy","du","shahabgh","karwan baxar", "farmgate", "bs","uttara"]

# for station in stations:
#    print("ehkon ahschen: ", station )


# ==========================================
# Rang in for loop
# ==========================================

# stations = ["motijheel","shochibaloy","du","shahabgh","karwan baxar", "farmgate", "bs","uttara"]

# for i in range(6):
#     print(stations[i])

# for i in range(2,7):
#     print(stations[i])

# ==========================================
# function definition
# ==========================================

# def breakfast(name,time, need_snacks):
#     print(f"Making breakfast for {name}")
#     if need_snacks:
#       print("Making snacks...")
#     print("Making coffee...")
#     print(f"Breakfast making done at {time}")
# breakfast("Hasan", "10:30 Am", True)

# ==========================================
# function definition with return
# ==========================================

# def breakfast(name,time, need_snacks):
#     print(f"Making breakfast for {name}")
#     if need_snacks:
#       print("Making snacks...")
#     print("Making coffee...")
#     print(f"Breakfast making done at {time}")
#     return f"all done"

# result = breakfast("", "",False)

# breakfast("Hasan", "10:30 Am", True)


# print(result)


# ==================================================
# function definition  example 2 (nested function)
# ==================================================

# def exec(f):
#     f(10,20)

# # def sum(a,b):
# #     print(a+b)

# def sub(a,c,):
#     print(a-c)

# exec(sub)


# ==========================================
# decorator
# ==========================================

# def home_decorator(func):
#     def rapper(pet_name):
#         print("welcome to the pet shop!")
#         func(pet_name)
#         print("welcome to the pet shop!")

#     return rapper
    
# @home_decorator
# def buy_bird(pet_name):
#     print(f"buying {pet_name}...")

# buy_bird("cat")


# ==========================================
# iterator
# ==========================================

# Fruits=["Apple", "Banana", "Cherry","Mango","orange"]
# f_itr= iter(Fruits)
# a= next(f_itr)
# print(a)
# b= next(f_itr)
# print(b)

# ==========================================
# generator
# ==========================================

# def get_next_id():
#     i = 0
#     while True:
#         yield i
#         i = i + 1

# random = get_next_id()

# number= next(random)
# print(number)

# for i in get_next_id(): ##Run an infinite loop
#     print(i)


# ==========================================
# arguments
# ==========================================

# def add(a,b,*args): 
#     print(a,b)
#     print(args)

# add(5,7)
# add(5,7,34,44,55,66)


# ==========================================
# keyword   arguments
# ==========================================


# def add(a,b,**kwargs): 
#     print(a,b)
#     print(kwargs)

# add(c=4, a=9, b=10,d=12)
