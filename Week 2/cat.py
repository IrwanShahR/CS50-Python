#while loop
i = 3
while i > 0:
    print("meow")
    i -= 1

#for loops
list = [4, 5, 6]
for i in list:
    print("Boo")


for i in range(5):
    print("Hello")

#print by default will already start a new line after
print("World\n" * 3, end="")


while True:
    x = int(input("Enter a positive number: "))
    if x < 0:
        continue
    else:
        break

for char in range(x):
    print("meow")