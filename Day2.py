import time

# ************************************** If Statements & logical operators ************************************** #
age = int(input("How old are you?"))

if age >= 18 and age < 120:
    print("You are an adult!")
elif age < 0 or age > 120:
    print("You are lying")
else:
    print("You are a child!")
    
# ************************************** While loops ************************************** #

name1 = ""

while(len(name1) == 0):
    name1 = input("Please enter your name: ")
    
print("Hello " + name1)

# ************************************** For Loops ************************************** #

for i in range(10):
    print(i + 10)
    
for i in range(50, 100):
    print(i)
    
for i in "Lewis Hamilton":
    print(i)
    
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(0.5)

print("Happy New Year!")


# ************************************** Nested loops ************************************** #

rows = int(input("Enter how many rows you would like: "))
coloumns = int(input("Enter how many coloumns you would like: "))
symbol = input("Please enter the symbol you would like to show: ")

for i in range(rows):
    for j in range(coloumns):
        print(symbol, end="")
    print()
    

# ************************************** Nested loops ************************************** #

while True:
    name = input("Please enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
    
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
        
# ************************************** 1D Lists ************************************** #

food = ["Beef" , "Chicken", "Pork"]
print(food[0])

for x in food:
    print(x)
    
food.append("Ice Cream") # Adds to the end of the list temproary
food.remove("Chicken") # Removes the specafied element
food.pop() # Removes the last element of the list
food.insert(0, "Cake") # Moves all up by 1 and takes the spot specafied 
food.sort() # Sortss the list alphabetically
food.clear() # clears the list

# ************************************** 2D Lists ************************************** #

drinks = ["coffee", "tea", "coke"]
dinner = ["beef", "chicken"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]
print(food[0])
print(food[1][1])

# ************************************** Tuple ************************************** #

student = ("Lewis", 35, "male")

print(student.count("Lewis"))
print(student.index("male"))

for x in student:
    print(x)
    
if "Lewis"in student:
    print("Lewis is here!")
    
# ************************************** Sets ************************************** #
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
utensils.update(dishes)

dinner_table = utensils.union(dishes)

print(utensils.difference(utensils))
print(utensils.intersection(dishes))

for x in utensils:
    print(x)
    
for i in dinner_table:
    print(i)
    
# ************************************** Dictionarys ************************************** #
Capitals = {'USA':'Washington', 
            'Ireland':'Dublin',
            "Japan":"Tokyo",
            "Korea":"Sendai"}

Capitals.update({"Germany":"Berlin"})
Capitals.update({"USA":"Las Vegas"})
Capitals.pop("Ireland")

print(Capitals["Japan"])
print(Capitals.get('Germany'))
print(Capitals.keys())
print(Capitals.values())
print(Capitals.items())

for key,value in Capitals.items():
    print(key, value)
    
# 1 : 47