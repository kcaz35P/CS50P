def main():
    print(fuel_gauge())

def fuel_gauge():
    while True:
        try:
            numerator, denominator = input("Fraction: ").split("/")
            fuel = (int(numerator) / int(denominator))*100
            if 1 < fuel < 99:
                return f"{fuel:.0f}" + '%'
            elif fuel in (0, 1):
                return "E"
            elif fuel in (99, 100):
                return "F"
            else:
                continue

        except (ValueError, ZeroDivisionError):
            pass

main()
