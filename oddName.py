"""Import the name and print all characters"""

name = input("Enter your name")

"""Check the name is not blank"""

while len(name) <= 0:
    print("Name is blank. Enter again")
    name = input("Enter your name")

#Print odd character in the name
print(name[1:len(name):2])
print(name[::2])

#Print odd character in the name
for i in range(0, len(name), 2):
    print(name[i])
