
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

# ************************************** Nested Function Calls ************************************** #

num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)
print(num)

#* does the same thing *#
print(round(abs(float(input("Enter a whole positive number: ")))))

# ************************************** Scope ************************************** #

def display_name():
    name1 = "Code"
    print(name1)
    
#* Cant print name1 outside 
display_name()

# ************************************** *args Parameter ************************************** #

def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0] = 0
    for i in stuff:
        sum+= i
    return sum

print(add(1,2,3,4,5,5,6,7,67,34546,7))

# ************************************** *kwargs ************************************** #

def hello2(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello", end = " ")
    for key,value in kwargs.items():
        print(value, end = " ")
    
hello2(first = "Lewis", middle = "P", last = "Hamilton")