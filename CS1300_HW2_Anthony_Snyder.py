first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
birth_year = int(input("Enter Birth Year: "))
favorite_hobby = input("Enter Favorite Hobby: ")
proper_first_name = first_name.title()
proper_last_name = last_name.title()
proper_hobby = favorite_hobby.title()
age = 2026 - birth_year
print("====================================")
print(         "USER PROFILE CARD")
print("====================================")
print("Name: ", proper_first_name, proper_last_name)
print("Age: ", age)
print("Hobby: ", proper_hobby)
print("------------------------------------")
print("Thank you for creating your profile!")
print("====================================")



print("=== TEXT ANALYZER ===")
sentence = input("Enter sentence: ")
print("--- Analysis Results ---")
total = len(sentence)
print("Total characters (with spaces): ", total)
no_spaces = sentence.replace(" ", "")
total_no_spaces = len(no_spaces)
print("Total characters (without spaces): ", total_no_spaces)
word_list = sentence.strip().split()
word_count = len(word_list)
print("Number of words: ", word_count)
def count_vowels_no_spaces(sentence):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    for char in no_spaces:
        if char in vowels:
            vowel_count += 1
    return vowel_count
result = count_vowels_no_spaces(sentence)
print("Number of vowels: ", result)
upper_case = sentence.upper()
print("Uppercase version: ", upper_case)
lower_case = sentence.lower()
print("Lowercase version: ", lower_case)
reversed_version = sentence[::-1]
print("Reversed: ", reversed_version)
capital_check = sentence[0].isupper()
print("Starts with capital: ", capital_check)
import string
def punctuation_check(sentence):
    if not sentence:
        return False
    last_char = sentence[-1]
    return last_char in string.punctuation
punctuation1 = punctuation_check(sentence)
print("Ends with punctuation: ", punctuation1)