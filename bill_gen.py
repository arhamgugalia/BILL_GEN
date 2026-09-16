"""Simple console-based restaurant bill generator."""

from __future__ import print_function

try:
	read_input = raw_input  # type: ignore[name-defined]
except NameError:
	read_input = input


MENU = {
	1: ("Veg Burger", 120.00),
	2: ("Pizza", 250.00),
	3: ("Pasta", 180.00),
	4: ("French Fries", 90.00),
	5: ("Soft Drink", 60.00),
	6: ("Ice Cream", 100.00),
}

TAX_RATE = 0.05


def show_menu():
	"""Display the available food items."""
	print("\n" + "=" * 42)
	print("             RESTAURANT MENU")
	print("=" * 42)
	for number, (name, price) in MENU.items():
		print("{0}. {1:<25} Rs. {2:>7.2f}".format(number, name, price))
	print("0. Finish order")


def read_quantity():
	"""Read a positive whole-number quantity from the customer."""
	while True:
		try:
			quantity = int(read_input("Quantity: "))
			if quantity > 0:
				return quantity
			print("Please enter a quantity greater than zero.")
		except ValueError:
			print("Please enter a whole number.")


def create_bill():
	"""Collect menu choices and return the selected items."""
	order = []

	while True:
		show_menu()
		try:
			choice = int(read_input("Choose an item: "))
		except ValueError:
			print("Please enter a menu number.")
			continue

		if choice == 0:
			return order
		if choice not in MENU:
			print("That item is not on the menu.")
			continue

		name, price = MENU[choice]
		quantity = read_quantity()
		order.append((name, quantity, price))
		print("Added {0} x {1}.".format(quantity, name))


def print_receipt(order):
	"""Print the final itemized receipt."""
	print("\n" + "=" * 52)
	print("                  RESTAURANT BILL")
	print("=" * 52)

	if not order:
		print("No items were ordered.")
		return

	subtotal = 0.0
	print("{0:<24}{1:>5}{2:>10}{3:>11}".format("Item", "Qty", "Price", "Amount"))
	print("-" * 52)
	for name, quantity, price in order:
		amount = quantity * price
		subtotal += amount
		print("{0:<24}{1:>5}{2:>10.2f}{3:>11.2f}".format(
			name, quantity, price, amount))

	tax = subtotal * TAX_RATE
	total = subtotal + tax
	print("-" * 52)
	print("{0:>41} Rs. {1:>7.2f}".format("Subtotal", subtotal))
	print("{0:>41} Rs. {1:>7.2f}".format("Tax (5%)", tax))
	print("{0:>41} Rs. {1:>7.2f}".format("TOTAL", total))
	print("=" * 52)
	print("Thank you for visiting!")


def main():
	"""Run the restaurant billing application."""
	print("Welcome to our restaurant!")
	order = create_bill()
	print_receipt(order)


if __name__ == "__main__":
	main()
