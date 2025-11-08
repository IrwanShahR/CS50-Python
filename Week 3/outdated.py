months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

delimiter = "/"

while True:
    date = input("Date: ")
    date = date.strip()

    try:
        if delimiter in date:
            datelist = date.split("/")
            day = int(datelist[1])
            month = int(datelist[0])
            year = (datelist [2])
        elif ", " in date:
            datelist = date.split()
            day = int(datelist[1].replace(",",""))
            month = int(months.index(datelist[0]))+1
            year = (datelist [2])
        else:
            raise ValueError
        
        if 0 < day <= 31 and 0 < month <= 12 and len(year) == 4:
            print(f"{int(year)}-{month:02}-{day:02}")
            break

    except (ValueError, IndexError):
        continue

