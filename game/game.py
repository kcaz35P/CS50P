
def main():

    guess()

def guess():

    from random import randint


    while True:
        try:
            n = int(input("Level: "))
            num = randint(1,n)
            while True:
                if n >= 0:
                    guess_num = int(input("Guess: "))
                    match guess_num:
                        case guess_num if guess_num > num:
                            print("Too large!")
                            continue
                        case guess_num if guess_num < num:
                            print("Too small!")
                            continue
                        case _:
                            print("Just right!")
                            exit (1)
        except ValueError:
            pass
main()
