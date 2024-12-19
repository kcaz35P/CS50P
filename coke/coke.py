def main():
    coke()

def coke():

    amount_due = 50
    values = [25, 10, 5]
    print("Amount Due:",amount_due)
    while amount_due > 0:
        money = int(input("Insert Coin: "))
        if money in values:
            amount_due -= money
            if(amount_due >0):
                print("Amount Due:",amount_due)
            else:
                print("Change Owed:", -amount_due)
        else:
            print("Amount Due:", amount_due)
main()

