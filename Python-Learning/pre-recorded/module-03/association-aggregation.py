class Laptop:
    def __init__(self, brand):
        self.brand = brand


class Student:
    def __init__(self, name, laptop_obj):
        self.name = name
        self.laptop_v = laptop_obj

    def show_laptop_info(self):
        print(f"{self.name} has a {self.laptop_v.brand} Laptop")


lp1 = Laptop("HP")
student = Student("Hasan", lp1)
student.show_laptop_info()


# Aggregation: Has-a relationship

class Department:
    def __init__(self, name):
        self.name = name


class University:
    def __init__(self, name):
        self.name = name
        self.departments = []

    def add_departments(self, department):
        self.departments.append(department)

    def show_departments(self):
        return [department.name for department in self.departments]


un1 = University("MIT")
dep1 = Department("Computer Science")
dep2 = Department("Math")

un1.add_departments(dep1)
un1.add_departments(dep2)

print(un1.show_departments())

#Composition

class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, brand, power):
        self.brand = brand
        self.engine = Engine(power)

    def show_details(self):
     print(f"{self.brand} has an engine with {self.engine.power} power") 

car = Car ('Toyota', 1800)

car.show_details()

      



