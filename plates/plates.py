def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s.isidentifier() == False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    for i in range (len(s)):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break

    i = len(s) - 1
    while i >= 0:
        if s[i].isalpha() == False:
            if s[i-1].isalpha() == True:
                if s[i-2].isalpha() == False:
                    return False
        if s[i].isalpha() == True:
            if s[i-1].isalpha() == False:
                return False
            return True
        i-=1

main()
