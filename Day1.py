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
print("Hello " + name2)
