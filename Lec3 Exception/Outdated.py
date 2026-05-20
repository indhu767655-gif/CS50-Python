months = [
    "January", "February","March","April","May","June",
    "July","August","September","October","November","December"
]

while True:
    date = input("Date:").strip()

    try:
        if "/" in date:
            m, d, y = map(int, date.split("/"))
        else:
            month, rest = date.split(" ", 1)
            d, y = rest.replace(",", "").split()
            m = months.index(month) + 1
            d, y = int(d), int(y)

        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y:04}-{m:02}-{d:02}")
            break
    except:
        print("Invalid format, try again.")
        pass


