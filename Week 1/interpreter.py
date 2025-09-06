write = input("Expression: ")

formatwrite = write.split(" ")

x = float(formatwrite[0])
y = formatwrite[1]
z = float(formatwrite[2])

if y ==  "+":
    print(round(x+z,1))
elif y == "-":
    print(round(x-z,1))
elif y == "*":
    print(round(x*z,1))
elif y == "/":
    print(round(x/z,1))


