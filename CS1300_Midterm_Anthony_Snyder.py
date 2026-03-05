weight = int(input("Enter weight: "))
unit_system = str(input("Enter unit system (M/I): "))
if unit_system.upper() == "M":
    height = float(input("Enter height (meters): "))
    bmi = (f"{weight / (height ** 2):.1f}")
elif unit_system.upper() == "I":
    height = int(input("Enter height (inches): "))
    bmi = f"{(weight * 703) / (height ** 2):.1f}"
else:
    bmi = 0
if float(bmi) > 0:
    if float(bmi) >= 30.0:
        category = "Obese"
    elif 29.9 >= float(bmi) >= 25.0:
        category = "Overweight"
    elif 24.9 >= float(bmi) >= 18.5:
        category = "Normal Weight"
    else:
        category = "Underweight"
    print("BMI: ", bmi)
    print("Category: ", category)
else:
    print("Invalid unit system.")




password = str(input("Enter password: "))
len_password = len(password)
uppercase = 0
lowercase = 0
digit = 0
special = 0
passes = []
fails = []
import string
special_chars = string.punctuation
for char in password:
    if char.isupper():
        uppercase += 1
    if char.islower():
        lowercase += 1
    if char.isdigit():
        digit += 1
    if char in special_chars:
        special += 1
if len_password >= 8:
    length = "PASS"
    passes.append(length)
else:
    length = "FAIL"
    fails.append(length)
if uppercase >= 1:
    uppercases = "Pass"
    passes.append(uppercases)
else:
    uppercases = "FAIL"
    fails.append(uppercases)
if lowercase >= 1:
    lowercases = "PASS"
    passes.append(lowercases)
else:
    lowercases = "FAIL"
    fails.append(lowercases)
if digit >= 1:
    digits = "PASS"
    passes.append(digits)
else:
    digits = "FAIL"
    fails.append(digits)
if special >= 1:
    special_char = "PASS"
    passes.append(special_char)
else:
    special_char = "Fail"
    fails.append(special_char)
count = len(passes)
if count == 5:
    strength = "Strong"
elif 4 >= count >= 3:
    strength = "Moderate"
elif 2 >= count >= 1:
    strength = "Weak"
else:
    strength = "No Password Entered"
print("Length >= 8: ", length)
print("Uppercase: ", uppercases)
print("Lowercase: ", lowercases)
print("Digit: ", digits)
print("Special char: ", special_char)
print("Criteria met: ", count,"/ 5")
print("Strength: ", strength)