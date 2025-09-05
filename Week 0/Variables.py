# ask user for their name
name = input("What's your name? ")
print("Hello,",name)
print("Hello, " + name)
print("Hello, ", end= "")
print(name)
print(f"Hello, {name}")
 # prints all the same. Print function takes another argument End


#remove white space from str. if user input "       Irwan"
name = name.strip()
print(f"Hello, {name}")

#capitalise the first char
name = name.capitalize()
print(f"Hello, {name}")