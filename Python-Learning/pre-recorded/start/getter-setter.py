class employee:
    def __init__(self, name, salary):
        self.name= name
        self._salary= salary

    def get_salary(self, password):
        if password == "admin":
            print(self._salary)
        else:
            print("Invalid Access!!")
    def set_salary (self, password, salary):
        if password == "admin":
            self._salary = salary
            print(f"New Salary is added: {self._salary}")
        else:
            print("Invalid Access!!")

ob1 = employee ("john",  30000)
ob2 = employee ("Rahim",  70000)


ob1.get_salary("123")
ob1.get_salary("admin")
ob1.set_salary("123", 50000)
ob1.set_salary("admin", 90000)

