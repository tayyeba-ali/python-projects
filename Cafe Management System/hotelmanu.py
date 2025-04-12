# Menu of restaurant
menu = {
    'Pasta': 300,
    'Pizza': 1500,
    'Burger': 500,
    'Sandwich': 200,
    'French Fries': 100,
    'Chocolate Cake': 250,
    'Ice Cream': 150,
    'Soda': 50,
    'Coffee': 100,
    'Tea': 50,
    'Juice': 80,
    'Water': 20,
}

# Greet the user
print("Welcome to the Cafe Management System!")
print("\nMenu:")
for item, price in menu.items():
    print(f" {item}: {price}")

order_total = 0
order_summary = {}

while True:
    item = input("\nEnter the name of the item you want to order: ").title()
    if item in menu:
        try:
            quantity = int(input(f"How many {item}s would you like to order? "))
            cost = menu[item] * quantity
            order_total += cost

            # Add to summary
            if item in order_summary:
                order_summary[item] += quantity
            else:
                order_summary[item] = quantity

            print(f"{quantity} x {item} added. Total so far: {order_total}")
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print(f"Sorry, {item} is not available in the menu.")

    another = input("Do you want to order another item? (Yes/No): ").strip().lower()
    if another != 'yes':
        break

# Final Summary
print("\n🧾 Order Summary:")
for item, qty in order_summary.items():
    print(f" {item} x {qty} = {menu[item] * qty}")

print(f"\nTotal to pay: {order_total}")
print("Thank you for visiting our cafe! Have a great day! ☕🍰")
