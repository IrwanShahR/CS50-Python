answer = input("What is the Answer to the Great Question of life, the Universen and Everything? ")


match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
