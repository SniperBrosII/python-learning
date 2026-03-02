temp = int(input("Enter temperature: "))
scale = str(input("Enter scale (C/F): "))
if scale.upper() == "C":
    print(f"{temp:.1f} C = {temp * 9/5 + 32:.1f} F")
elif scale.upper() == "F":
    print(f"{temp:.1f} F = {(temp - 32) * 5/9:.1f} C")
else:
    print("Invalid scale.")




sentence = str(input("Enter a sentence: "))
total_chars = len(sentence)
uppercase_count = 0
lowercase_count = 0
digit_count = 0
space_count = 0
for char in sentence:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char == " ":
        space_count += 1
reversed = sentence[::-1]
print("Total characters: ", total_chars)
print("Uppercase letters: ", uppercase_count)
print("Lowercase letters: ", lowercase_count)
print("Digits: ", digit_count)
print("Spaces: ", space_count)
print("Reversed: ", reversed)