# Unit 1.1 Exercises

## Beginner
my_info = {
    'name': 'Anthony',
    'age': '18',
    'major': 'Cybersecurity'
}
print(my_info)

## Intermediate
prices = dict(burger=8.99, fries=3.49, chicken_sandwich=7.99, onion_rings=3.49)
print(prices)
course_credits = {
    'IIT1000': '1',
    'CS1300': '3',
    'IIT2000': '0',
    'CS1350': '3'
}
print(course_credits)

## Advanced
weekly_temps = dict(Sunday=76, Monday=75, Tuesday=78, Wednesday=82, Thursday=83, Friday=82, Saturday=79)
print(weekly_temps)


#Unit 1.2 Exercises

## Beginner
pet = {"name": "Buddy", "type": "dog", "age": 3}
print(pet["name"])
print(pet["age"])

## Intermediate
print(pet.get("color", "Unknown"))
grades = {
    "Alice": 85,
    "Bob": 63,
    "Charlie": 48
}
student = "Charlie"
grade = grades.get(student, 0)
if grade >= 60:
    print(f"{student} passed the course.")
elif grade == 0:
    print(f"{student} not found.")
else:
    print(f"{student} did not pass the course.")

## Advanced
products = {"laptop": 999.99, "mouse": 29.99, "keyboard": 79.99}
def find_price(product_name):
    price = products.get(product_name)
    if price is not None:
        print(f"${price:.2f}")
    else:
        print("Product not available.")
print(products)
find_price(str(input("Please select a product: ")))


# Unit 1.3 Exercises

## Beginner
inventory = {}
inventory["apples"] = 10
inventory["oranges"] = 3
inventory["bananas"] = 6
print(inventory)

## Intermediate
scores = {"Team A": 45, "Team B": 38}
scores["Team B"] = 52
scores["Team C"] = 41
dropped = scores.pop("Team A")
print(f"Team A Final Score: {dropped}")

## Advanced
cart = {}
cart["T-Shirt"] = 24.99
cart["Hoodie"] = 69.99
cart["Sweatpants"] = 41.99
cart["Hoodie"] = 63.99
removed = cart.pop("T-Shirt")
print(f"Final cart: {cart}")


#Unit 2.1 Exercises

## Beginner
### Which of these are valid dictionary keys? Write "valid" or "invalid" and explain why:
"student_name" # Valid (reason: it is a string which means it is immutable.)
[1, 2, 3] # Invalid (reason: it is a list which is mutable and cannot be a dictionary key.)
100 # Valid (reason: numbers are immutable allowing them to be dictionary keys.)
("x", "y") # Valid (reason: tuples are immutable allowing them to be dictionary keys.)
{"a": 1} # Invalid (reason: dictionaries are mutable meaning they cannot be dictionary keys.)
frozenset({1, 2}) # Valid (reason: "frozenset" creates an immutable set of data meaning it can be a dicitonary key.)

## Intermediate
### 1. This code has an error. Find and fix it:

# locations = {[40.7, -74.0]: "New York", [34.0, -118.2]: "Los Angeles"}

#### The error is that lists cannot be used as dictionary keys.

#### Fixed code using tuples:
locations = {(40.7, -74.0): "New York", (34.0, -118.2): "Los Angeles"}

### 2. What will this print? Predict the output, then verify:
data = {"a": 1, "b": 2, "a": 3, "b": 4}
print(data)
print(len(data))

#### Output: 
# "a": 3, "b": 4
# 2

### 3. Investigate: What is the hash value of your name? What about the number 100?
print(f"Hash value of 'Anthony': {hash('Anthony')}")
print(f"Hash value of '100': {hash(100)}")


## Advanced
### 1.
tracker = {}
tracker["Jon", "Space Invaders"] = 218870
tracker["Blue", "Tetris"] = 40264954
tracker["Billy", "Pac-Man"] = 3333360
high_score = tracker.get(("Jon", "Space Invaders"), "Player not found.")
print(high_score)

### 2.
import time
numbers_list = list(range(100_000))
numbers_dict = {i: True for i in range(100_000)}
target = 99_999
start = time.perf_counter()
target in numbers_list
list_time = time.perf_counter() - start
start = time.perf_counter()
target in numbers_dict
dict_time = time.perf_counter() - start
print(f"List search time: {list_time:.10f} seconds")
print(f"Dictionary search time: {dict_time:.10f} seconds")
if list_time < dict_time:
    print(f"List is faster by {dict_time - list_time:.10f} seconds.")
else:
    print(f"Dictionary is faster by {list_time - dict_time:.10f} seconds.")


#Unit 2.2 Exercises

## Beginner
temps = {"Monday": 72, "Tuesday": 75, "Wednesday": 68}
print(temps.keys())
print(temps.values())
print(len(temps.keys()))

## Intermediate
highest = max(temps.values())
lowest = min(temps.values())
print(highest)
print(lowest)
if "Friday" in temps:
    print(temps)
else:
    print("Friday is not found.")
temps.setdefault("Thursday", 70)
key_view = temps.keys()
print(key_view)
temps.setdefault("Friday", 66)
print(key_view)

## Advanced
import sys
items = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
total = sum(items.values())
average = total / len(items.values())
maximum = max(items.items(), key=lambda item: item[1])
minimum = min(items.items(), key=lambda item: item[1])
print(f"Total value: ${total}")
print(f"Average price: ${average:.2f}")
print("Most expensive:", maximum[0], "$" + str(maximum[1]))
print("Least expensive:", minimum[0], "$" + str(minimum[1]))
items_view = items.keys()
items_list = list(items.keys())
dict_memory = sys.getsizeof(items_view)
list_memory = sys.getsizeof(items_list)
print(f"Memory used by items.keys(): {dict_memory} bytes")
print(f"Memory used by list(items.keys()): {list_memory} bytes")
if dict_memory < list_memory:
    print(f"items.keys() is using {list_memory - dict_memory} less bytes.")
else:
    print(f"list(items.keys()) is using {dict_memory - list_memory} less bytes.")
items.update({
    "headphones": 199,
    "camera": 799,
    "speaker": 149
})
print("\nALL products:")
for piece, item in items.items():
    print(piece, "$" + str(item))

# Unit 2.3 Exercises

## Beginner
colors = {"apple": "red", "banana": "yellow", "grape": "purple"}
for fruit, color in colors.items():
    print(f"The {fruit} is {color}.")
# This will return three tuples containing a fruit and its color.
print(list(colors.items()))

## Intermediate
drinks = {"coffee": 4.50, "tea": 3.00, "juice": 5.25}
for item, drink in drinks.items():
    tax_price = drink * 1.10
    print(f"{item}: ${drink:.2f} + tax = ${tax_price:.2f}")
count = 0
for item, drink in drinks.items():
    if drink > 4.00:
        count += 1
print("Items over $4.00:", count)
x = 10
y = 20
x, y = y, x
print("x = ", x)
print("y = ", y)
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print("First: ", first)
print("Middle: ", middle)
print("Last: ", last)

## Advanced
exams = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
import time
highest_student, highest_exam = max(exams.items(), key = lambda item: item[1])
print("Highest score:", highest_student, "-", highest_exam)
passed = {}
failed = {}
for student, exam in exams.items():
    if exam >= 70:
        passed[student] = exam
    else:
        failed[student] = exam
print("Passed: ", passed)
print("Failed: ", failed)
avg = sum(exams.values()) / len(exams)
deviations = {}
for student, exam in exams.items():
    deviations[student] = exam - avg
print("Class average: ", avg)
print("Deviations: ", deviations)
large_scores = {f"Student{i}": i for i in range(50_000)}
start = time.perf_counter()
for student, large_score in large_scores.items():
    pass
items_time = time.perf_counter() - start
start = time.perf_counter()
for student in large_scores.keys():
    large_score = large_scores[student]
keys_time = time.perf_counter() - start
print("\nPerformance Test:")
print(f"items() iteration: {items_time:.6f} seconds")
print(f"keys() + lookup: {keys_time:.6f} seconds")
if items_time < keys_time:
    difference = keys_time - items_time
    print(f"items() is faster by {difference:.6f} seconds")
else:
    difference  = items_time - keys_time
    print(f"keys() + lookup is faster by {difference:.6f} seconds")