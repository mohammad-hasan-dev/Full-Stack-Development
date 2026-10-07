
class grandfather:
    def __init__(self):
            self.name= "Rahim"
            self._age= 30
            self.__gold = 5000
    def greet(self):
        print("Form Grandfather")

class father(grandfather):
    def greet(self):
        print(f"Form father, Name: {self.name}, age:{self._age}, Has gold: {self._grandfather__gold} ")
class children(father):
    def greet(self):
        print("Form Children")


fat= father()

fat.greet()
