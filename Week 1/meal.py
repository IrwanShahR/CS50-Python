def main():
    user = input("What time is it? ")
    convertedtime = convert(user)

    if convertedtime >= 7 and convertedtime <= 8:
        print("breakfast time")
    elif convertedtime >= 12 and convertedtime <= 13:
        print("lunch time")
    elif convertedtime >= 18 and convertedtime <= 19:
        print("dinner time")



def convert(time):
    time = time.split(":")

    x = float(time[0])
    y = float(time[1])/60
    z = float(round(x + y,2))
    return z




if __name__ == "__main__":
    main()





