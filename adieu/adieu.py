import inflect
p = inflect.engine()

def main():
    adieu()

def adieu():
    names = []

    while True:
        try:
            name = input("Enter a Name:")
            names.append(name)
        except EOFError:
            print("Adieu, adieu, to " + p.join(names))
            break

if __name__ == "__main__":
    main()
