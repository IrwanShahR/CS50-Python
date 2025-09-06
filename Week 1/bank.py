greeting = input("Greeting: ")

if greeting.strip().lower() == "hello":
    print("$0")
elif "hello" in greeting.strip().lower():
    print("$0")
elif greeting[0].lower() == "h":
    print("$20")

else:
    print("$100")



