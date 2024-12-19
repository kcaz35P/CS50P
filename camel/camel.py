def main():
    camel = input("CamelCase: ")
    print(camelCase(camel))


def camelCase(camelCase):
    snakeCase = ""
    for i in camelCase:
        if (i.isupper()):
            snakeCase += "_" + i.casefold()
        else:
            snakeCase += i
    return snakeCase

main()
