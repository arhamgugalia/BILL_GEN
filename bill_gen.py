print("===== RESTAURANT BILL =====")

name = input("Enter your name: ")

total = 0

while True:
    print("\nMenu")
    print("1. Burger - Rs. 120")
    print("2. Pizza - Rs. 250")
    print("3. Pasta - Rs. 180")
    print("0. Finish Order")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        break

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
        continue

    amount = price * quantity
    total = total + amount

    print(f"{item} x {quantity} = Rs. {amount}")

tax = total * 0.05
final_amount = total + tax

print("\n===== BILL =====")
print(f"Customer Name: {name}")
print(f"Subtotal: Rs. {total:.2f}")
print(f"Tax (5%): Rs. {tax:.2f}")
print(f"Total: Rs. {final_amount:.2f}")
print("Thank you for visiting!")

