# Exceptions = Errors


try:
    print(x)
except:
    print("An error occurred")
finally:
    print("success")

num1 = 20
num2 = 0

try:
    print(num1 / num2)
except:
    print("Zero division error occurred")


# User-defined functions
try:
    def multiply(number1, number2):
        print(number1 * number2)

except:
    print("Error occured")
finally:
    print("Success")

multiply(6, 5)
