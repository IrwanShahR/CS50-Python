name = input("What's your name? ")

#you can you if elif statements

#but here's another method. Using MATCH

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    
    #this is for whoever else not defined above
    case _:
        print("Who?")