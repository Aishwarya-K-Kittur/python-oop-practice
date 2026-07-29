class Student:
    school = "ABC school"

    @classmethod
    def change_school(cls, school):
        cls.school = school

    def __init__(self, name, age):
        self.name = name
        self.age = age


    def display(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"school: {self.school}")

    def have_birthday(self):
        self.age += 1

    @staticmethod
    def is_adult(age):
        return age >= 18

    

# student1 = Student("Aishwarya", 25)
# student1.have_birthday()
# student1.display()

# Student.change_school("XYZ international schools")
# print(Student.school)

print(Student.is_adult(20))
print(Student.is_adult(17))

