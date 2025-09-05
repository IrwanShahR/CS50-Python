def convert(string):
    return string.replace(":)","🙂").replace(":(", "🙁")

def main():
    user = str(input("Input string here: "))
    user = convert(user)
    print(user)

main()
