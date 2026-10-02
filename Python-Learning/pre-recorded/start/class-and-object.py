

# class car:
#     def __init__(self):
#         self.brand =""
#         self.model= ""


# car1= car()
# car1.brand= "Toyota"
# car1.model= "2025"

# print(car1.brand,"=",car1.model)

#__init__ dunder Method, constructor
#constructor is 3 types
# Default constructor, parameterized constructor, default value constructor


class car:
    def __init__(self): # Default constructor
        self.brand =""
        self.model= ""

    def __init__(self,brand,model):  #parameterized constructor
        self.brand= brand
        self.model= model

    def __init__(self,brand="Toyota",model="2025"): #default value constructor
        self.brand=brand
        self.model=model
    


car1= car()

print(car1.brand,"=",car1.model)

# Method inside




