# try:
#     # code that might raise an exception
# except:
#     # runs if there WAS an exception
# else:
#     # runs IF and ONLY IF there was NO exception

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x =  int(input("What's x? "))
        except ValueError:
            #print("You typed an invalid number")
            pass #catch the error, but wont do anything
        else:
            break
    return x


main()