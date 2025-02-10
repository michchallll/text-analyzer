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
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print("-" * 40)
else:
    print("Unregistered user, terminating the program...")
    exit()