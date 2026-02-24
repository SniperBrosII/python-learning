a = int(input("Please enter the first integer: "))
b = int(input("Please enter the second integer: "))
c = int(input("Please enter the third integer: "))
x = (not (a > b or b > c))
y = (a <= b and b <= c)
print(a < b < c)
print(not (a > b or b > c))
print(a <= b and b <= c)
if x == y:
    print("De Morgan's confirmed: Expressions 2 and 3 match!")
else:
    print("De Morgan's not confirmed: Expressions 2 and 3 do not match.")




temp = int(input("Enter temperature: "))
rain = int(input("Is it raining? (Yes = 1, No = 0): "))
if temp > 100:
    print("EXTREME HEAT WARNING: Stay indoors!")
elif temp > 85 and rain == 1:
    print("Warm rain - watch for flash floods.")
elif temp > 85 and rain == 0:
    print("Hot and dry - stay hydrated.")
elif 65 <= temp <= 85 and rain == 1:
    print("Grab an umbrella!")
elif 65 <= temp <= 85 and rain ==0:
    print("Nice weather - enjoy your day!")
elif 32 <= temp <= 59:
    print("It's cold - bundle up!")
else:
    print("FREEZE WARNING: Roads may be icy!")




name = str(input("Please enter your name: "))
exam1 = int(input("Please enter score for exam 1: "))
exam2 = int(input("Please enter score for exam 2: "))
exam3 = int(input("Please enter score for exam 3: "))
scores = [exam1, exam2, exam3]
average = sum(scores) / len(scores)
if 90 <= average <= 100:
    grade = "A"
elif 87 <= average <= 89:
    grade = "A-"
elif 83 <= average <= 86:
    grade = "B+"
elif 80 <= average <= 82:
    grade = "B"
elif 77 <= average <= 79:
    grade = "B-"
elif 73 <= average <= 76:
    grade = "C+"
elif 70 <= average <= 72:
    grade = "C"
elif 67 <= average <= 69:
    grade = "C-"
elif 63 <= average <= 66:
    grade = "D+"
elif 60 <= average <= 62:
    grade = "D"
else:
    grade = "F"
if average >= 90:
    standing = "Dean's List"
elif average >= 70:
    standing = "Good Standing"
elif average >= 60:
    standing = "Academic Probation"
else:
    standing = "Academic Suspension Warning"
print("============================")
print("    Student Grade Report")
print("============================")
print("Student: ", name)
print("Exam 1: ", exam1)
print("Exam 2: ", exam2)
print("Exam 3: ", exam3)
print("----------------------------")
print("Average: ", average)
print("Grade: ", grade)
print("Status: ", standing)
print("============================")