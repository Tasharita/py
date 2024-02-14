#Datatype

number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
is_Python_Interesting = True  # bool

#A variable with multiple values
language = ["Python", "php", "java", "kotlin"]  # list
fruits = ("apple", "banana", "pineapple")  # Tuple
countries = {"Kenya", "Ghana", "China"}  # Set

#DICTIONARY
details = {
    "Firstname" : "Ashley",
    "course" : "MIT",
    "Age" : 18,
    "nationality" : "USA"
}

print(number)
print(num)
print(greeting)
print(is_Python_Interesting)
print(countries)
print(details)
print(details["Firstname"])
print(details["nationality"])

# Determining the data type of a variable
print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting - Converting one data to another
print(float(number))
print(int(num))