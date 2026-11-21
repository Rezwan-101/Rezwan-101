months = [
    "January", "February", "March",
    "April", "May", "June",
    "July", "August", "September",
    "October", "November", "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

        else:
            month, day, year = date.split(" ")

            month = months.index(month.capitalize()) + 1

            if not day.endswith(","):
                continue
            day = int(day[:-1])
            
            year = int(year)

        if month < 1 or month >12:
            continue

        if day < 1 or day > 31:
            continue

        print(f"{year:04}-{month:02}-{day:02}")
        break


    except ValueError:
        continue

