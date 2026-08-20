age = int(input("Please enter your age: "))
matinee = str(input("Is the showing a matinee? (yes/no): "))
is_true = True if matinee.lower() == 'yes' else False
if age > 0:
    if age > 65:
        group = "Senior"
        if is_true == True:
            price1 = 6
        else:
            price1 = 7
    elif 18 <= age <= 64:
        group = "Adult"
        if is_true == True:
            price1 = 8
        else:
            price1 = 13
    elif 13 <= age <= 17:
        group = "Teen"
        if is_true == True:
            price1 = 7
        else:
            price1 = 10
    else:
        group = "Child"
        if is_true == True:
            price1 = 6
        else:
            price1 = 8
else:
    print("Invalid Age")
print("Age group: ", group)
print("Ticket Price: $",f"{price1:.2f}")




student_id = str(input("Enter Student ID: "))
name = str(input("Enter name: "))
number = int(input("Enter age: "))
major = str(input("Enter major (CS/IT/CE/DS): "))
errors = []
len_true = True if len(student_id) == 8 else False
character_true = True if student_id[0].isalpha() else False
digit_true = True if student_id[1:9].isdigit() else False
name_true = True if name.isspace() else False
try:
    if not (16 <= number <= 99):
        raise ValueError("Age is outside the specified range.")
except ValueError as e:
    number_true = False
else:
    number_true = True
if major.lower() in ["cs", "it", "ce", "ds"]:
    major_true = True
else:
    major_true = False
entry1 = "Student ID must be exactly 8 characters (got",len(student_id),")"
entry2 = "Major must be one of the following: CS, IT, CE, DS (got",major,")"
if len_true == False:
    errors.append(entry1)
if character_true == False:
    errors.append("Student ID must start with a letter")    
if digit_true == False:
    errors.append("Student ID must have 7 digits following the first letter")
if name_true == True:
    errors.append("Name cannot be empty")
if number_true == False:
    errors.append("Age must be a valid integer between 16 and 99")
if major_true == False:
    errors.append(entry2)
if errors == []:
    print("Profile created successfully!")
    print("Student ID: ", student_id)
    print("Name: ", name)
    print("Age: ", number)
    print("Major: ", major)
else:
    print("Profile has errors:")
    for item in errors:
        print(item)




print("==============================")
print("  Campus Campus Order System")
print("==============================")
print("   1. Coffee       - $3.50")
print("   2. Sandwich     - $6.00")
print("   3. Salad        - $5.50")
print("   4. Combo        - $8.00")
print("   5. Exit")
print("==============================")
price = 0
choice = int(input("Enter your choice (1-5): "))
if choice == 1:
    price = price + 3.50
    size = str(input("What size? (S/M/L): "))
    if size.upper in ["S", "M", "L"]:
        if size == "M":
            price = price + 1.00
        elif size == "L":
            price = price + 2.00
        else:
            price = price
    else:
        size = "S"
        print("Invalid size: defaulting to S")
elif choice == 2:
    cheese = str(input("Add cheese? (y/n): "))
    if cheese == "y":
        price = price + 6.75
    else:
        price = price + 6.00
elif choice == 3:
    dressing = str(input("Choose a dressing (ranch, italian, vinaigrette, none): "))
    if dressing.lower in ["ranch", "italian", "vinaigrette", "none"]:
        price = price + 5.50
    else:
        price = price + 5.50
        dressing = "none"
        print("Invalid dressing: defaulting to none")
elif choice == 4:
    price = price + 8.00
    size = str(input("What size coffee? (S/M/L): "))
    if size.upper in ["S", "M", "L"]:
        if size == "M":
            price = price + 1.00
        elif size == "L":
            price = price + 2.00
        else:
            price = price
    else:
        size = "S"
        print("Invalid size: defaulting to S")
    cheese = str(input("Add cheese to sandwich? (y/n): "))
    if cheese == "y":
        price = price + 0.75
else:
    print("Successfully exited menu.")
customer = str(input("Enter your name: "))
quantity = int(input("How many? "))
try:
    if (quantity > 0):
        quantity_true = True
    else:
        quantity_true = False
except ValueError:
    quantity_true = False
if quantity_true == False:
    print("Invalid number.")
    quantity = int(input("How many? "))
subtotal = price * quantity
tax = subtotal * 0.07
total = subtotal + tax
print("==============================")
print("        Order Receipt")
print("==============================")
print("Customer: ", customer)
if choice == 1:
    if size == "S":
        print("Item: Small Coffee")
    elif size == "M":
        print("Item: Medium Coffee")
    else:
        print("Item: Large Coffee")
elif choice == 2:
    if cheese == "y":
        print("Item: Sandwich + Cheese")
    else:
        print("Item: Sandwich")
elif choice == 3:
    if dressing == "ranch":
        print("Item: Salad + Ranch Dressing")
    elif dressing == "italian":
        print("Item: Salad + Italian Dressing")
    elif dressing == "vinaigrette":
        print("Item: Salad + Vinaigrette Dressing")
    else:
        print("Item: Salad + No Dressing")
else:
    if size == "S":
        if cheese == "y":
            print("Item: Small Coffee + Sandwich + Cheese")
        else:
            print("Item: Small Coffee + Sandwich")
    elif size == "M":
        if cheese == "y":
            print("Item: Medium Coffee + Sandwich + Cheese")
        else:
            print("Item: Medium Coffee + Sandwich")
    else:
        if cheese == "y":
            print("Item: Large Coffee + Sandwich + Cheese")
        else:
            print("Item: Large Coffee + Sandwich")
print("Quantity: ", quantity)
print("Unit Price: $",f"{price:.2f}")
print("Subtotal: $",f"{subtotal:.2f}")
print("Tax (7%): $",f"{tax:.2f}")
print("Total: $"f"{total:.2f}")
print("==============================")
print()
print("Thank you for your order!")