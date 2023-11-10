prices = {'chicken': 8.50,
          'steak': 13.80,
          'fish': 9.80,
          'pasta': 9.50,
          'coffee': 2.50,
          'tea': 1.80,
          'water': 0.50}

orders = {}

def showmenu():
    print()
    print("-----------------------")
    print("1. Add Order")
    print("2. Summarize Orders")
    print("3. Quit")
    print("-----------------------")

def showprice():
    print("Food Items\tPrice")
    for item, price in prices.items():
        print(f"{item}\t\t{price}")

def add_order():
    print("\nFood Items\tPrice")
    for item, price in prices.items():
        print(f"{item}\t\t{price}")
    
    item = input("\nEnter the item to order: ")
    if item in prices:
        quantity = int(input("Enter the number of sets to order: "))
        if item in orders:
            orders[item] += quantity
        else:
            orders[item] = quantity
        print("Order added successfully!")
    else:
        print("Invalid item. Please try again.")

def summarize_orders():
    if not orders:
        print("No orders have been placed yet.")
    else:
        print("\nSummary of Orders")
        print("Item\t\tQuantity")
        for item, quantity in orders.items():
            print(f"{item}\t\t{quantity}")

while True:
    showmenu()
    choice = input("Your Choice: ")
    
    if choice == '1':
        add_order()
    elif choice == '2':
        summarize_orders()
    elif choice == '3':
        print("Thank you for using the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
