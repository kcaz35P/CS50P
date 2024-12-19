def main():
    greetings = input("Greeting: ").strip().casefold()
    if "hello" in greetings:
        print("$0")
    elif greetings.startswith("h") == True:
        print ("$20")
    else:
        print ("$100")
main ()
