def main():
    difficulty = input("Difficult or Casual? ")
    players = input("Multiplater or Singleplayer? ")

    if difficulty == "Difficult":
        if players == "Multiplayer":
            recommend("Poker")
        else:
            recommend("Klondike")
    elif difficulty == "Casual":
        if players == "Multiplayer":
            recommend("Hearts")
        else:
            recommend("Clock")
    else:
        print("Enter a valid difficulty")



def recommend(game):
    print("I would recommend " + game + ".")



main()