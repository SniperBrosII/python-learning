sizes = ["Personal", "Medium", "Large", "Party"]
order_descriptions = []
order_prices = []
subtotal = 0
personal_counter = 0
medium_counter = 0
large_counter = 0
party_counter = 0
discount_counter = 0
print("Welcome to to the CS 1300 Pizza Shop!")
answer = str(input("Would you like to order a pizza? (yes/no): "))
while answer.lower() == "yes" or answer.lower() == "y":
    payment = 0
    print("=============================")
    print("         PIZZA SIZES")
    print("=============================")
    price = 3.99
    inch = 4
    for i in range(len(sizes)):
        if i <= 2:
            price = price + 3
        else:
            price = price + 4
        inch = inch + 4
        print(f"{i+1}. {sizes[i]}", f"({inch} in.)", f"{"$":>5}"f"{price:.2f}")
    print("=============================")
    choice = str(input("Pick a size (1-4): "))
    while choice.isdigit() is False:
        print("Please enter a number!")
        choice = str(input("Pick a size (1-4): "))
    while 1 > int(choice) or int(choice) > 4:
        print("Choose 1-4.")
        choice = str(input("Pick a size (1-4): "))
    if choice == "1":
        size = "Personal (8 in.)"
        base_price = 6.99
        personal_counter += 1
    elif choice == "2":
        size = "Medium (12 in.)"
        base_price = 9.99
        medium_counter += 1
    elif choice == "3":
        size = "Large (16 in.)"
        base_price = 12.99
        large_counter += 1
    else:
        size = "Party (20 in.)"
        base_price = 16.99
        party_counter += 1
    selected_toppings = []
    available_toppings = ["Pepperoni", "Mushrooms", "Green Peppers", "Onions", "Sausage", "Bacon", "Extra Cheese", "Pineapple"]
    print("Available toppings ($1.50 each):")
    for i in range(len(available_toppings)):
        print(f"{i+1}. {available_toppings[i]}")
    topping = str(input("Add topping # (or 'done'): "))
    while topping != "done":
        if 1 <= int(topping) <= 8:
            if available_toppings[int(topping) - 1] in selected_toppings:
                print("Already added", available_toppings[int(topping) - 1],"!")
                topping = str(input("Add topping # (or 'done'): "))
                continue
            else:
                selected_toppings.append(available_toppings[int(topping) - 1])
                print("Added", available_toppings[int(topping) - 1])
                topping = str(input("Add topping # (or 'done'): "))
        else:
            print("Choose a topping # (1-8).")
            topping = str(input("Add topping # (or 'done'): "))
    payment = base_price + (len(selected_toppings) * 1.50)
    if selected_toppings == []:
        selected_toppings.append("Cheese")
    order_descriptions.append(size)
    order_descriptions.append(selected_toppings)
    order_prices.append(payment)
    answer = str(input("Order another pizza? (yes/no): "))
discount = str(input("Do you have a discount code? ('none' to skip): "))
discount_counter += 1
while discount_counter < 3:
    if discount.upper() == "STUDENT10":
        discount = 0.90
        break
    elif discount.upper() == "HALFOFF":
        discount = 0.50
        break
    elif discount.upper() == "NONE":
        discount = 1
        break
    else:
        print("Invalid code.")
        discount_counter += 1
        discount = str(input("Do you have a discount code? ('none' to skip): "))
if discount_counter == 3:
    discount = 1
    print("No discount applied.")
if not order_descriptions:
    print("No pizzas ordered. See you next time!")
else:
    print("====================================")
    print("          YOUR ORDER RECEIPT")
    print("====================================")
    for i in range(0, len(order_descriptions), 2):
        print(f"{(i//2)+1}. {order_descriptions[i]}, {order_descriptions[i+1]}")
        print(f"{'$':>31}{order_prices[i//2]:.2f}")
    print("------------------------------------")
    for i in range(len(order_prices)):
        subtotal = subtotal + order_prices[i]
    tax = subtotal * 0.07
    total = (subtotal + tax) * discount
    saving = (subtotal + tax) - (total)
    print("Subtotal:", f"{'$':>21}{subtotal:.2f}")
    print("Tax (7%):", f"{'$':>21}{tax:.2f}")
    print("Discount:", f"{'$':>21}{saving:.2f}")
    print("Total:", f"{'$':>24}{total:.2f}")
    print("====================================")
    print("  Thank you for your order!")
    expensive = max(order_prices)
    max_index = order_prices.index(expensive)
    print(f"Most expensive pizza: {order_descriptions[max_index*2]}, {order_descriptions[max_index*2+1]}")
    print(f"Price: ${order_prices[max_index]:.2f}")
    cheap = min(order_prices)
    min_index = order_prices.index(cheap)
    print(f"Cheapest pizza: {order_descriptions[min_index*2]}, {order_descriptions[min_index*2+1]}")
    print(f"Price: ${order_prices[min_index]:.2f}")
    print("==============================")
    print("        Size Breakdown")
    print("==============================")
    print("Number of Personal Pizzas: ", personal_counter)
    print("Number of Medium Pizzas: ", medium_counter)
    print("Number of Large Pizzas: ", large_counter)
    print("Number of Party Pizzas: ", party_counter)
    print("------------------------------")
    print("Thank you for your order!")