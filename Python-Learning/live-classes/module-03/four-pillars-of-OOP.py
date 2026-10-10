#=========================
#Multilevel inheritance
#=========================

# class bc_account:
#     def withdraw(self):
#         print("Money Withdrawn")

# class sv_ac(bc_account):
#     def save(self):
#         print("Save Money with Saving Account!")

# class ultra_sv_ac(sv_ac):
#     def save_ultra(self):
#         print("Ultra Money with Ultra Account!")




# ba= bc_account()
# ba.withdraw()
# usa= ultra_sv_ac()
# usa.withdraw()
# usa.save()
# usa.save_ultra()

#=========================
# Multiple inheritance
#=========================
# class bc_account:
#     def withdraw(self):
#         print("Money Withdrawn")

# class no_charge:
#     def free_fee(self):
#      print("No charge free")

# class sv_ac(bc_account):
#     def save(self):
#         print("Save Money with Saving Account!")


# class student_account(no_charge, bc_account):
#     pass


# class ultra_sv_ac(sv_ac):
#     def save_ultra(self):
#         print("Ultra Money with Ultra Account!")




# st= student_account()
# st.withdraw()
# st.free_fee()

#=========================
# Access modifiers
#=========================
# class example:
#     a=5 #public
#     _b=7 #protected
#     __c= 10 # Private

#=========================
# Polimorphism
#=========================
# class bank_account:
#     def withdraw(self):
#         print("Money withdrawn!")

# class Saving_account:
#     def withdraw(self):
#         print("Money withdrawn from savings account!")

# sa= Saving_account()
# sa.withdraw()


#=========================
# Abstract class
#=========================

# from abc import ABC, abstractmethod


# class bankaccount(ABC):
#     @abstractmethod
#     def withdraw(self):
#         pass

# class saving_ac(bankaccount):
#     def withdraw(self):
#         pass
# class current_ac(bankaccount):
#     def withdraw(self):
#         pass
# class student_ac(bankaccount):
#     def withdraw(self):
#         pass

# class farmer_ac(bankaccount):
#     def withdraw(self):
#         pass

# fm= farmer_ac()
# fm.withdraw()

#===========================
# Singleton Design pettern
#===========================

# class db_connection:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

# a= db_connection()
# b= db_connection()
# c= db_connection()

# print(a)
# print(b)
# print(c)

#===========================
# Builder Design pettern
#===========================
# class computer:
#      def __init__(self,cpu,ram,storage):
#           self.cpu=cpu
#           self.ram=ram
#           self.storage=storage

#      def __str__(self):
#           return f"computer with {self.cpu} cpu, {self.ram} ram, {self.storage} storage."
          
      

# class computerbuilder:
#     def __init__(self):
#         self.cpu = None
#         self.ram = None
#         self.storage = None

#     def set_cpu(self,cpu):
#         self.cpu=cpu
#         return self
#     def set_ram(self, ram):
#         self.ram = ram
#         return self
#     def set_storage(self,storage):
#         self.storage = storage
#         return self
                     
#     def build(self):
#          return computer(self.cpu, self.ram, self.storage)

# builder =computerbuilder()

# computer = builder.set_cpu("intel i9").set_ram("32GB").set_storage("5 tb").build()
# print(computer)

#===========================
# Factory Design pettern
#===========================

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


