# class is a bluprint of an object
# an object is an instance of class

class Person:
    # properties/ attributes / characteristics
    name = "Bob"
    age = 23
    location = "Westlands"

    def speak(self):
      print("Person is speaking")

accountant = Person()
print(accountant.age)

accountant.speak()

