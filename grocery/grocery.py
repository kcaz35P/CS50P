def main():
    items_cart()

def items_cart():
    cart = dict() ## Initiallize an Empty Dictionary
    while True:
        try:
            product = input("").upper() ## Prompts the user for input and Convert to All UPPERCASE
            if product in cart: ## Check the existing Key
                cart[product] += 1 ## Increment the value/quantity
            elif product not in cart: ## In case of not Existing Key
                cart.update({product:1}) ## Add Product/Key and value
        except EOFError:
            for key, value in sorted(cart.items()): #Sort Keys, Accessing Key and Values
                print(value,key)
            break
        except KeyError:
            pass

main()
