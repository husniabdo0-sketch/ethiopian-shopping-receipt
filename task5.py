def get_required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a name; it cannot be blank.")


def get_price(prompt):
    while True:
        try:
            price = float(input(prompt))
            if price < 0:
                print("Price cannot be negative. Please try again.")
            else:
                return price
        except ValueError:
            print("Please enter a valid number, such as 100 or 12.50.")


def get_quantity(prompt):
    while True:
        try:
            quantity = int(input(prompt))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
            else:
                return quantity
        except ValueError:
            print("Please enter a whole number, such as 1 or 3.")


print("=" * 48)
print("                    RECEIPT")
print("=" * 48)

customer = get_required_text("Customer name: ")

product1 = get_required_text("First product name: ")
price1 = get_price("First product price in ETB: ")
quantity1 = get_quantity("First product quantity: ")

product2 = get_required_text("Second product name: ")
price2 = get_price("Second product price in ETB: ")
quantity2 = get_quantity("Second product quantity: ")

item_total1 = price1 * quantity1
item_total2 = price2 * quantity2
total = item_total1 + item_total2

print()
print(f"Customer: {customer}")
print()
print(f"{'Product':<18}{'Price':>10}{'Qty':>7}{'Amount':>13}")
print("-" * 48)
print(f"{product1:<18}{price1:>10.2f}{quantity1:>7}{item_total1:>13.2f}")
print(f"{product2:<18}{price2:>10.2f}{quantity2:>7}{item_total2:>13.2f}")
print("-" * 48)
print(f"Total: {total:.2f} ETB")
print("Thank you for shopping!")
print("=" * 48)