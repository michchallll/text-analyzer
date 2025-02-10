"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Michael Kubát
email: michchallll@gmail.com
discord: michchallll
"""

import task_template

# Přihlašovací údaje registrovaných uživatelů
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Přihlášení uživatele
username = input("Enter your username: ")
password = input("Enter your password: ")

if username in users and users[username] == password:
    print("-" * 40)
    print(
        f"Welcome to the app, {username}\n"
        f"We have 3 texts to be analyzed."
    )
    print("-" * 40)
else:
    print("Unregistered user, terminating the program...")
    exit()

# Výběr textu
try:
    text_choice = int(input("Enter a number btw. 1 and 3 to select: "))
    if text_choice not in [1, 2, 3]:
        print("Invalid choice, terminating the program...")
        exit()
except ValueError:
    print("Invalid input, terminating the program...")
    exit()

selected_text = task_template.TEXTS[text_choice - 1]
words = selected_text.split()

# Počítání statistik
word_count = len(words)
titlecase_count = sum(1 for word in words if word.istitle())
uppercase_count = sum(1 for word in words if word.isupper() and word.isalpha())
lowercase_count = sum(1 for word in words if word.islower())
numeric_count = sum(1 for word in words if word.isdigit())
numeric_sum = sum(int(word) for word in words if word.isdigit())

print("-" * 40)
print(
    f"There are {word_count} words in the selected text.\n"
    f"There are {titlecase_count} titlecase words.\n"
    f"There are {uppercase_count} uppercase words.\n"
    f"There are {lowercase_count} lowercase words.\n"
    f"There are {numeric_count} numeric strings.\n"
    f"The sum of all the numbers is {numeric_sum}"
)
print("-" * 40)

# Histogram délek slov
word_lengths = {}
for word in words:
    cleaned_word = word.strip(".,!?")  # Odstranění interpunkce
    length = len(cleaned_word)
    if length in word_lengths:
        word_lengths[length] += 1
    else:
        word_lengths[length] = 1

print("LEN|  OCCURENCES  |NR.")
print("-" * 40)
for length, count in sorted(word_lengths.items()):
    print(f"{length:3}|{'*' * count:<14}|{count}")