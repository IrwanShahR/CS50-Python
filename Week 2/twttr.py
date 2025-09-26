x = input("Input: ")

str = ""
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for char in x:
    if char not in vowels:
        str += char
print(str)