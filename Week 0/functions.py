def hello():
    print("Hello, " + name)


name = input("What's your name? ")
hello()


#passing an argument into the function
def hello(to):
    print("Hello,", to)

name = input("What's your name? ")
hello(name)

hello("everyone")


#returning value from a function
def main():
    x = int(input("Input a number: "))
    print("x squared is", square(x))
    
def square(n):
    return n*n

main()