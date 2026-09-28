class Student:
    def __init__(self, name, student_id, email, age, department, marks=None):
        self.name = name
        self.student_id = student_id
        self.__email = email
        self.age = age
        self.department = department
        self.__marks = marks if marks is not None else []

    @property
    def email(self):
        return self.__email

    @property
    def marks(self):
        return self.__marks

    def display_info(self):
        print("\n--- Student Information ---")
        print(f"Name: {self.name}")
        print(f"Student ID: {self.student_id}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Department: {self.department}")

    def calculate_result(self, *marks):
        if marks:
            self.__marks = list(marks)

        if not self.__marks:
            return 0

        return sum(self.__marks) / len(self.__marks)

    def get_student_type(self):
        return "General Student"


class UndergraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        semester,
        marks=None
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            marks
        )

        self.semester = semester

    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Semester: {self.semester}")


class GraduateStudent(Student):
    def __init__(
        self,
        name,
        student_id,
        email,
        age,
        department,
        research_topic,
        marks=None
    ):
        super().__init__(
            name,
            student_id,
            email,
            age,
            department,
            marks
        )

        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")



student1 = Student(
    "Rahim",
    "ST001",
    "rahim@example.com",
    20,
    "Computer Science",
    [80, 85, 90]
)

student2 = UndergraduateStudent(
    "Karim",
    "ST002",
    "karim@example.com",
    21,
    "Software Engineering",
    5,
    [75, 82, 88]
)

student3 = GraduateStudent(
    "Hasan",
    "ST003",
    "hasan@example.com",
    25,
    "Computer Science",
    "Artificial Intelligence",
    [90, 92, 95]
)




student1.display_info()
print("Student Type:", student1.get_student_type())
print("Result:", student1.calculate_result())


student2.display_info()
print("Student Type:", student2.get_student_type())
print("Result:", student2.calculate_result())


student3.display_info()
print("Student Type:", student3.get_student_type())
print("Result:", student3.calculate_result())




print("\n--- Polymorphism ---")

students = [student1, student2, student3]

for student in students:
    print(student.get_student_type())




print("\n--- Method Overloading ---")

print("One mark:", student1.calculate_result(80))
print("Two marks:", student1.calculate_result(80, 90))
print("Three marks:", student1.calculate_result(80, 90, 100))