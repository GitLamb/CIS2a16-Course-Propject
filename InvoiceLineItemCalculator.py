#Jason Lambert
#CIS261
#InvoiceLineItemCalculator

def get_price():
    while True:
        try:
            return float(input("Enter price: "))
        except ValueError:
            print("Invalid price format. Please enter a valid number.")

def get_quantity():
    while True:
        try:
            return int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity format. Please enter a whole number.")

def display_total(price, quantity):
    total = price * quantity
    print(f"\nPrice: ${price:.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total: ${total:.2f}\n")

def main():
    while True:
        price = get_price()
        quantity = get_quantity()
        display_total(price, quantity)

        cont = input("Enter another line item? (y/n): ").strip().lower()
        if cont != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()