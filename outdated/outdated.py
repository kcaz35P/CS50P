def main():
    convert_datef()

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
def convert_datef():
    while True:
        try:
            date = input("Date:").title().strip()

            if '/' in date:
                month, day, year = date.split('/')
                if month not in months:
                    day = int(day)
            elif ',' in date:
                date, year = date.split(', ')
                month, day = date.split(' ')
                day = int(day)
            try:
                if int(month) <= 12:
                    ...
            except (ValueError):
                if (month in months) and months.index(month) <12:
                    month = months.index(month) + 1
                    pass
            month = int(month)
            if month <= 12 and day <= 31:
                return print(f"{year}-{month:02}-{day:02}", end="")

        except (ValueError, TypeError, UnboundLocalError):
            pass
main()
