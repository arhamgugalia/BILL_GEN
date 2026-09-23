print("===== RESTAURANT BILL =====")

name = input("Enter your name: ")

print("\nMenu")
print("1. Burger - Rs. 120")
print("2. Pizza - Rs. 250")
print("3. Pasta - Rs. 180")

choice = int(input("Enter your choice: "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Burger"
    price = 120
elif choice == 2:
    item = "Pizza"
    price = 250
elif choice == 3:
    item = "Pasta"
    price = 180
else:
    print("Invalid choice")
    exit()

amount = price * quantity
tax = amount * 0.05
total = amount + tax

print("\n===== BILL =====")
print(f"Customer Name: {name}")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Price: Rs. {price}")
print(f"Amount: Rs. {amount}")
print(f"Tax (5%): Rs. {tax:.2f}")
print(f"Total: Rs. {total:.2f}")
print("Thank you for visiting!")
