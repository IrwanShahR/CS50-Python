# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print("Welcome to the secret auction program")

def find_highest_bidder(bids):
    highest_bidder = ""
    highest_bid = 0
    for i in bids:
        if dict[name] > highest_bid:
            highest_bid = dict[i]
            highest_bidder = i

    print(f"The highest bidder is {highest_bidder} with a bid of {highest_bid}")

dict = {}
to_continue = True
while to_continue:
    name = input("What is your name?: ")
    bid = int(input ("What's your bid?: "))

    dict[name] = bid

    others = str(input("Are there any other bidders? Type yes or no.\n"))
    if others.strip() == 'yes':
        print("\n" * 20)
    if others.strip() == 'no':
        to_continue = False
        find_highest_bidder(dict)


