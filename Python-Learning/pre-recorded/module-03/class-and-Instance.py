# class School:
#     school_name =" Cpa high school" # global class veriable

#     def __init__(self, name): #instance veriable
#         self.student_name=name

# student1= School("Mohamad")
# student2= School("Ali")
# print(student1.school_name, " : ",student1.student_name)
# print(student2.school_name, " : ",student2.student_name)


# class and instance methods

from logging import info


class Employee:
    company_name=" Meta Company "
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display_info(self):
        print(f"EMP Name : {self.name} \nSalary : {self.salary} ")

    @classmethod 
    def change_comany_name(cls,name):
        cls.company_name=name

emp1 = Employee("Rahim", 15000)
emp2= Employee("Karim", 25000)
emp1.change_comany_name("Google Company")
emp1.display_info()
emp2.display_info()
print(emp1.company_name)