import random

def main():
    level = get_level()
    generate_integer(level)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1, 4):
                raise ValueError
            else:
                return level
        except ValueError:
            pass

def generate_integer(level):
    counter = 0
    score = 0

    if level == 1:
        low_limit, high_limit = 0, 9
    elif level == 2:
        low_limit, high_limit = 10, 99
    else:
        low_limit, high_limit = 100, 999

    while counter < 10:
        tries = 0

        num1 = random.randint(low_limit, high_limit)
        num2 = random.randint(low_limit, high_limit)
        total = num1 + num2

        while tries < 3:
            try:
                answer = int(input(f"{num1} + {num2} = "))
                if answer == total:
                    score += 1
                    counter += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")

        if tries == 3:
            print(f"{num1} + {num2} = {total}")
            counter += 1

    print(f"Score: {score}")

if __name__ == "__main__":
    main()
