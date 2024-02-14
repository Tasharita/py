# Inbuilt functions
y = max(67, 56, 34, 23, 89)
print(y)

x = min(12, 36, 56, 79, 1)
print(x)

z = pow(2, 3)
print(z)

# user-defined functions
def details ():
    print("Hello")

details() # calling a function

# parametres and argument
def students(name, course, age):
    print(name, course, age)

students ("Ashley", "MIT", "17")
students("Goretty", "Cybersecurity", "18")

# fullname id salary position age

def employees(Fullname, IDno, Salary, Position, age):
    print(Fullname, IDno, Salary, Position, age)

employees ("Mitchelle", "89754", "ksh60000", "Manager", "23")
employees("Joy", "374645", "Ksh650000", "Chief Executive", "25")
employees("Natalie", "37786", "Ksh800000", "Director", "35")
employees("Jasmine", "73871", "Ksh730000", "CEO", "42")
employees("Charles", "129445", "Ksh900000", "Manager", "45")
