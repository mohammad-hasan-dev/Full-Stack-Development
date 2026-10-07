#single inheritence

# class Grandfather:
#     def __init__ (self, color, f_name):
#         self.color = color
#         self.f_name = f_name

# class father(Grandfather): #single inheritence
#     def __init__(self, hobby, color, f_name):
#         super().__init__(color, f_name)
#         self.hobby = hobby


# gf1 = Grandfather("white", "jamal")
# gf2= father("Cricket", "Black", "Ali")

# print(f"{gf1.color},{gf1.f_name}" )
# print(f"{gf2.color},{gf2.f_name}, {gf2.hobby}" )

# Multiple inherintence
# class Grandfather:
#     def __init__ (self, color, f_name):
#         self.color = color
#         self.f_name = f_name
#     def gf_method(self):
#         print("I am form Grandfather")

# class father(Grandfather): #single inheritence
#     def __init__(self, hobby):
#         self.hobby = hobby
#     def ft_method(self):
#             print("I am form Father")

# class son(father, Grandfather): #multiple inheritence
#     def __init__(self, fashion, hobby, color, f_name):
#         father.__init__(self, hobby)
#         Grandfather.__init__(self, color, f_name)
#         self.fashion = fashion
         
# son1 = son("Artist", "Football", "Red", "Chowdhury")
# son1.gf_method()
# son1.ft_method()
# print(son1.fashion, son1.hobby, son1.color, son1.f_name)




#Multi Level  inheritence

# class Grandfather:
#     def __init__ (self, color, f_name):
#         self.color = color
#         self.f_name = f_name
#     def gf_method(self):
#         print("I am form Grandfather")

# class father(Grandfather): #single inheritence
#     def __init__(self, hobby, color, f_name):
#         super().__init__(color, f_name)
#         self.hobby = hobby
#     def ft_method(self):
#             print("I am form Father")

# class son(father, Grandfather): #multiple inheritence
#     def __init__(self, fashion, hobby, color, f_name):
#          super().__init__(hobby, color, f_name)
#          self.fashion = fashion
         
# son1 = son("Artist", "Football", "Red", "Chowdhury")
# son1.gf_method()
# son1.ft_method()
# print(son1.fashion, son1.hobby, son1.color, son1.f_name)

# Hierarchical Inheritance

class Vehicle:
    def engine_type(self):
        print ("Vehicle has an engine")

class car (Vehicle):
    def num_doors(self):
        print("Car  Has 4 doors")

class Truck(Vehicle):
    def load_capacity(self):
        print("Truck can carry 10 tons")

car = car()
car.engine_type()
car.num_doors()
truck = Truck()
truck.load_capacity()

# hybrid Inheritance

class Shape:
    def area(self):
        print("Calculating area...")

class polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides.")

class Rectangel(polygon):
    def __init__(self,lenght, breadth):
        self.length = lenght
        self. breadth = breadth

    def area(self):
        return self.length*self.breadth

rec= Rectangel(10,5)
rec.sides()
print(rec.area())
rec.area()