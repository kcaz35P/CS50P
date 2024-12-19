def main():
    taqueria_menu()

def taqueria_menu():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        try:
            total += menu[input("Item: ").casefold().title()]
            print(f"Total: ${total:.2f}")
        except (ValueError, KeyError):
            pass
        except (EOFError):
            break

main()


