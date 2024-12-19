def main():
    words = input("Input:")
    omit(words)

def omit(words):
    vowels = ["a","e","i","o","u","A","E","I","O","U"] #list for omitted vowels
    omitted = "" # initializing the string variable

    for consonant in words:
       if consonant not in vowels:
            omitted += consonant
    print(omitted)
main()


