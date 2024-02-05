
# ************************************** String Formats ************************************** #

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item)) 
print("The {1} jumped over the {0}".format(animal, item)) 
print("The {star} jumped over the {an}".format(an = "Sheep", star = "Sun")) 

text = "The {} jumped over the {}"

print(text.format(animal, item))

name = "Lewis"
print("Hello my name is {}".format(name))
print("Hello my name is {:10}.Nice To meet you.".format(name))
print("Hello my name is {:>10}.Nice To meet you.".format(name))
print("Hello my name is {:^10}.Nice To meet you.".format(name))

number = 1000

print("The number pie is {:.2f}".format(number)) # decimal points
print("The number pie is {:,}".format(number)) 
print("The number pie is {:b}".format(number)) #binary
print("The number pie is {:o}".format(number)) # 
print("The number pie is {:X}".format(number)) # Hexedecimal
print("The number pie is {:E}".format(number)) # Scientific Notation