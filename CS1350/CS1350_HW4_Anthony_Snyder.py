# Unit 3.1 Exercises
## Beginner
inventory = {"apples": 50, "bananas": 30, "oranges": 25}
for product in inventory:
    print(product)
total_items = sum(inventory.values())
print(f"Total items: {total_items}")
for product, quantity in inventory.items():
    print(product, quantity)

## Intermediate
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
for product in sorted(prices):
    print(product)
for product, price in sorted(prices.items(), key=lambda item: item[1]):
    print(product, price)
most_expensive = max(prices.items(), key=lambda item:item[1])
print("Most expensive:", most_expensive[0], most_expensive[1])

## Advanced
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}
avg = sum(temps.values()) / len(temps.values())
print(f"Average temp: {avg:.1f}")
hottest = 0
coldest = float("inf")
for day, temp in temps.items():
    if temp > hottest:
        hottest = temp
        hottest_day = day
    elif temp < coldest:
        coldest = temp
        coldest_day = day
    else:
        pass
print(f"Hottest day: {hottest_day} ({hottest})")
print(f"Coldest day: {coldest_day} ({coldest})")
above_average = 0
for temp in temps.values():
    if temp > avg:
        above_average += 1
print(f"Days above average: {above_average}")


# Unit 3.2 Exercises
## Beginner
products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}
print("Laptop price:", products["laptop"]["price"])
for product, details in products.items():
    print(product, "stock:", details["stock"])
    
## Intermediate
countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]
nations = {}
for country, capital in zip(countries, capitals):
    nations[country] = capital
products["tablet"] = {"price": 449, "stock": 30}
for product in list(products.keys()):
    if products[product]["stock"] < 20:
        del products[product]
print(products)

## Advanced
company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}
for department, employees in company.items():
    print(department)
    for employee, salary in employees.items():
        print(" ", employee, salary)
for department, employees in company.items():
    avg = sum(employees.values()) / len(employees)
print(f"{department} average salary: {avg:.0f}")
highest_employee = None
highest_salary = 0
highest_department = None
for department, employees in company.items():
    for employee, salary in employees.items():
        if salary > highest_salary:
            highest_salary = salary
            highest_employee = employee
            highest_department = department
print(f"Highest paid employee: {highest_employee}")
print(f"Department: {highest_department}")
print(f"Salary: {highest_salary}")


# Unit 3.3 Exercises
## Beginner
cubes = {num: num ** 3 for num in range(1, 6)}
print(cubes)
temps = {"Mon": 72, "Tue": 68, "Wed": 75}
celcius = {
    day: (temp - 32) * 5 / 9
    for day, temp in temps.items()
}
for day, temp in celcius.items():
    print(f"{day}: {temp:.1f} C")

## Intermediate
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}
passing = {
    student: score
    for student, score in scores.items()
    if score >= 70
}
print(f"Passing: {passing}")
letter_grades = {
    student: (
        "A" if score >= 90 else
        "B" if score >= 80 else
        "C" if score >= 70 else
        "D" if score >= 60 else
        "F"
    )
    for student, score in scores.items()
}
print(f"Letter grades: {letter_grades}")
student_ids = {"Alice": 101, "Bob": 102}
ids_to_students = {
    student_id: student
    for student, student_id in student_ids.items()
}
print(f"IDs to students: {ids_to_students}")

## Advanced
sales = [
    ("North", "Alice", 5000), ("South", "Bob", 4500),
    ("North", "Carol", 6000), ("South", "Alice", 3500)
]
region_totals = {}
salesperson_totals = {}
for region, salesperson, amount in sales:
    region_totals[region] = region_totals.get(region, 0) + amount
    salesperson_totals[salesperson] = salesperson_totals.get(salesperson, 0) + amount
print(f"Sales by region: {region_totals}")
print(f"Sales by salesperson: {salesperson_totals}")
nested = {}
for region, person, amount in sales:
    if region not in nested:
        nested[region] = {}
    nested[region][person] = nested[region].get(person, 0) + amount
print(nested)


# Unit 4.1 Exercises
## Beginner
vowels = {"a", "e", "i", "o", "u"}
print(vowels)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
number_set = set(numbers)
print(number_set)
print(len(number_set))
# empty = {} is an empty dictionary not an empty set
# to make an empty set you must make it "empty = set()"

## Intermediate
text = "mississippi"
unique_chars = set(text)
print(unique_chars)
print(len(unique_chars))
emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]
unique_emails = list(set(emails))
print(unique_emails)
# s = {[1, 2], [3, 4]} fails because lists cannot be elements of a set

## Advanced
import time
numbers_list = list(range(1_000_000))
number_set = set(numbers_list)
start = time.time()
999999 in numbers_list
list_time = time.time() - start
start = time.time()
999999 in number_set
set_time = time.time() - start
print(f"List lookup time: {list_time}")
print(f"Set lookup time: {set_time}")
my_set = frozenset(["apple", "banana", "orange"])
my_dict = {
    my_set: "A collection of fruits"
}
print(my_dict)
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]
nodes = {node for edge in edges for node in edge}
print(nodes)


# Unit 4.2 Exercises
## Beginner
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
union = a | b
print(f"Union: {union}")
intersection = a & b
print(f"Intersection: {intersection}")
difference = a - b
print(f"Difference: {difference}")

## Intermediate
morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}
all_shifts = morning_shift & evening_shift & weekend_shift
print(f"All shifts: {all_shifts}")
any_shift = morning_shift | evening_shift | weekend_shift
print(f"At least one shift: {any_shift}")
only_morning = morning_shift - evening_shift - weekend_shift
print(f"Morning only: {only_morning}")
exactly_one = (
    (morning_shift - evening_shift - weekend_shift)
    | (evening_shift - morning_shift - weekend_shift)
    | (weekend_shift - morning_shift - evening_shift)
)
print(f"Exactly one shift: {exactly_one}")

## Advanced
prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}
eligible = prereqs_met & has_space & paid_tuition
print(f"Eligible: {eligible}")
not_paid = prereqs_met - paid_tuition
print(f"Met prereqs but haven't paid: {not_paid}")
all_students = prereqs_met | has_space | paid_tuition
needs_something = all_students - (prereqs_met & paid_tuition)
print(f"Needs prereqs or tuition: {needs_something}")


# Unit 4.3 Exercises
## Beginner
numbers = {1, 2, 3}
numbers.add(4)
numbers.remove(1)
print(numbers)
even_numbers = {x for x in range(21) if x % 2 == 0}
print(even_numbers)
numbers = {1, 2, 3}
numbers.discard(5)
print(numbers)

## Intermediate
numbers = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]
unique_numbers = list(dict.fromkeys(numbers))
print(unique_numbers)
sentence = "To be or not to be that is the question"
unique_words = [word.lower() for word in sentence.split()]
print(unique_words)
expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}
missing = expected - actual
print(missing)

## Advanced
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates
print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))
alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}
all_three = alice & bob & carol
print(f"All three: {all_three}")
only_alice = alice - bob - carol
print(f"Only Alice: {only_alice}")
all_skills = alice | bob | carol
print(f"All skills: {all_skills}")
def common_chars(str1, str2):
    return set(str1) & set(str2)
print(common_chars("hello", "world"))