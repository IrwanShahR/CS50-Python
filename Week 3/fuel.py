
def check_int():
    while True:
        try:
            fuel = input("Fraction: ")
            text = fuel.split("/")
            num = int(text[0])
            den = int(text[-1])
            try:
                if num <= den and num > 0 and den > 0:
                    return round((num/den)*100)
            except:
                pass
        except:
            pass


def result():
    x = check_int()
    if x <= 1:
        print("E")
    elif x >= 99:
        print("F")
        print(f"Debug: x = {x}")
    else:
        print(f"{x}%")

result()