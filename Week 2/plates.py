# #In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

# “All vanity plates must start with at least two letters.” done
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.” done
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.” done
# “No periods, spaces, or punctuation marks are allowed.” done
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, 
# wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif spec_char(s) == False:
        return False
    elif check_first_chars(s) == False:
        return False
    elif check_first_number(s) == False:
        return False
    elif numbers_middle(s) == False:
        return False
    else:
        return True
    
def spec_char(x):
    for char in x:
        if char.isalpha() == False and char.isdigit() == False:
            return False

def check_first_chars(x):
    if x[0:2].isalpha() == False:
        return False
    
def check_first_number(x):
    for char in x:
        if char.isdigit() == True: 
            if int(char) == 0:
                return False
            else:
                break

def numbers_middle(x):
    for char in x:
        if char.isdigit()== True:
            if x.index(char) < (len(x)-2):
                return False
main()