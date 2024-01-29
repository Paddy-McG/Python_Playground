print("Hello World!")
print("Hello World again!")

# ************************************** Variables ************************************** #
firstName = "Patrick"
lastName = "McGonagle"
fullName = firstName + " " + lastName
# Prints the type of the variable to the console
print(type(firstName))

print("Hello " + firstName)
print("Hello " + fullName)


age1 = 21
age1 += 1
print("Your age is "  + str(age1))

height = 250.5
print("Your height is: " + str(height) + "cm")
print(type(height))

human = False
print("Are you a human: " + str(human))


# ************************************** Multiple Assignment ************************************** #
name, championships, goat = "Lewis Hamilton", 7, True

Spongebob = Patrick = Sandy = 30

print(len(name))
print(name.find("o"))
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("i"))
print(name.replace("o" , "A"))
print(name * 3)


# ************************************** Type Casting ************************************** #
x = 1
y = 2.0
z = "3"

print(x)
print(y)
print(z)

y = int(y)
print(y)
print(x*3)


# ************************************** Taking in User input ************************************** #
name2 = input("What is your name? ")
age2 = int(input("Please enter your age: "))
height = float(input("Please enter your height: "))

print("Hello " + name2)
print("You are " + str(age2) + " years old")
print("You are " + str(height) + "cm tall")


# ************************************** Math ************************************** #
import math

pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(420))
print(max(x, y, pi))
print(min(x, y, pi))


# ************************************** Slicing ************************************** #
name = "LewisHamilton"

first_name = name[0:5]
last_name = name[6:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)