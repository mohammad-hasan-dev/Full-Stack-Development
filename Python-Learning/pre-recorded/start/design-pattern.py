# Singleton Design Pattern

# class singleton:
#     _instance = None

#     def __new__(cls):
       
#         if cls._instance is None:
#             cls._instance = super(singleton,cls).__new__(cls)
#             print("1st object created")
#         return cls._instance


# ob1 = singleton()
# ob2 = singleton()

# print(ob1 is ob2)

# factory Design Pattern

# class car:
#     def driver(self):
#         return("Driving a car")

# class bike:
#     def driver(self):
#         return("riding a bike")
# class vehiclefactory():
#     @staticmethod
#     def get_vehicle(type):
#         if type == "car":
#             return car()
#         elif type == "bike":
#          return bike()
#         else:
#             return ValueError(" Unknown Vehicle")


# vehicle =vehiclefactory.get_vehicle("bike")

# print(vehicle.driver())

# Builder Design Pattern
class computer:
     def __init__(self,cpu,ram,storage):
          self.cpu=cpu
          self.ram=ram
          self.storage=storage

     def __str__(self):
          return f"computer with {self.cpu} cpu, {self.ram} ram, {self.storage} storage."
          
      

class computerbuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self,cpu):
        self.cpu=cpu
        return self
    def set_ram(self, ram):
        self.ram = ram
        return self
    def set_storage(self,storage):
        self.storage = storage
        return self
                     
    def build(self):
         return computer(self.cpu, self.ram, self.storage)

builder =computerbuilder()

computer = builder.set_cpu("intel i9").set_ram("32GB").set_storage("5 tb").build()
print(computer)
