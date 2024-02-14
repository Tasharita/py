class Person:
    def __init__(self, firstname, age, gender):
        self.firstname = firstname
        self.age = age
        self.gender = gender

    def details(self):
        print(self.firstname, "is studying")

teacher = Person("Joy", 23,"Female")
accountant = Person("Joe", 56, "Male")
doctor = Person("Salome" , 34, "Female")

print(teacher.firstname, teacher.age, teacher.gender)
doctor.details()