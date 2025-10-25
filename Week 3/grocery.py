list = {}
while True:
    try:
        item = input("").upper()

        if item != "":
            if item in list:
                count = list[item]
                list[item] = count +1
            else:
                list[item] = 1
    except EOFError:
            break

sorted = sorted(list.items())
new_list= dict(sorted)
for i in new_list:
    print(f"{new_list[i]} {i}")
