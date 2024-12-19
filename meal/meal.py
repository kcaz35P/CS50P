def main():
    meal()
def meal():
    time = input("Enter a Time(24-hour format): ")
    match convert(time):
        case time if 7 <= time <= 8:
            print("breakfast time")
        case time if 12 <= time <= 13:
            print("lunch time")
        case time if 18 <= time <= 19:
            print("dinner time")

def convert(time):
    hour, min = time.split(":")
    min = int(min) / 60
    new_hour = int(hour) + min
    str(new_hour)
    return new_hour

if __name__ == "__main__":
    main()
