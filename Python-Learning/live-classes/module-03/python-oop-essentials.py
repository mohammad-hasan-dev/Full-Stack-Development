# class student: #---> class

#     def set_name(self, n):
#         self.name= n

#     def say_hello (self): # objecct / Instance method
#         print(f"Hello, {self.name} !")
        
# a= student()
# b= student()

# a.name= "Hasan" #---> instance veriable

# a.set_name("zayed")
# a.say_hello()

# =========================
# With constructor
# =========================

# class student: #---> class

#     def __init__(self, n): # ---> __init__ constructor
#         self.name= n

#     def say_hello (self): # objecct / Instance method
#         print(f"Hello, {self.name} !")
        
# a= student("Hasan")
# b= student("jhon")

# a.say_hello()
# b.say_hello()

# =========================
# Class veriable
# =========================

# class bankac:
#     sent_fee =10

# a =bankac()
# b =bankac()
# c =bankac()

# a.sent_fee=30
# print(a.sent_fee)
# print(b.sent_fee)
# print(c.sent_fee)


# =========================
# Class Method
# =========================

# class bc_account:
#     send_fee = 20

#     @classmethod
#     def update_send_fee(cls, new_sf):
#        cls.send_fee = new_sf
  
# bc_account.update_send_fee(30)
# a = bc_account

# print(a.send_fee)

# =========================
# static Method
# =========================

# class bc_account:
#     def __init__(self,owner, number):
#         self.owner=owner
#         self.number=number

#     @staticmethod
#     def valid_num(n):
#         if len(n)==11:
#          return "its a valid number"
#         else:
#            return "its an invalid number"


# print(bc_account.valid_num("12345678910"))

# print(bc_account.valid_num("123456710"))

# print(bc_account.valid_num("12345678345435910"))

# =========================
# Getter & Setter
# =========================

# class bc_account:
#     def __init__(self, owner):
#      self.owner=owner
#      self._balance=10

#      @property
#      def balance(self):
#         ...
#         return self._balance

#      @balance.setter
#      def balance(self, new_balance):
#         ...
#         self._balance= new_balance

# d= bc_account("jhon")

# print(d._balance)

    