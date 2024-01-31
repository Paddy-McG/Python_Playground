
# ************************************** Index Operator ************************************** #

name = "lewis hamilton"

if (name[0].islower()):
    name = name.capitalize() # Capatalises the first letter
    
first_name = name[:5].upper()
last_name = name[6:].lower()
last_character = name[-1]

print(last_character)
print(last_name)
print(first_name)
print(name)

# ************************************** Functions ************************************** #

def hello(name1, age):
    print("Hello " + name1)
    print("You are " + str(age) + " years old")
    print("Have a nice day!")
    
my_name = "Paddy"
    
hello("Lewis", 21)
hello(my_name, 18)

# ************************************** Return statement ************************************** #

def multiply(number1, number2):
    return number1 * number2

x = multiply(1256, 45)

print(multiply(6,8))
print(x)

# ************************************** Keyword Arguments ************************************** #

def hello1(first,middle,last):
    print("Hello " + first + " " + middle + " " + last)
    
hello1(last = "McG", middle = "James" , first = "Paddy")