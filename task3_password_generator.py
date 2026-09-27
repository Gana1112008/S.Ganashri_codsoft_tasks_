"""
CODSOFT - Python Programming Internship
Task 3: Password Generator

Lets the user specify the desired password length and which
character sets to include (uppercase, lowercase, digits, symbols),
then generates and displays a strong random password.
"""

import random
import string


def get_length():
    """Ask the user for a valid password length."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Length must be a positive number.")
                continue
            return length
        except ValueError:
            print("Please enter a valid whole number.")


def get_yes_no(prompt):
    """Ask a yes/no question and return True/False."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please answer with 'y' or 'n'.")


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Build a character pool from the selected options and return a
    random password of the requested length."""
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return None  # no character types were selected

    return "".join(random.choice(char_pool) for _ in range(length))


def main():
    print("========== PASSWORD GENERATOR ==========")

    length = get_length()
    use_upper = get_yes_no("Include uppercase letters? (y/n): ")
    use_lower = get_yes_no("Include lowercase letters? (y/n): ")
    use_digits = get_yes_no("Include numbers? (y/n): ")
    use_symbols = get_yes_no("Include symbols? (y/n): ")

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    if password is None:
        print("\nYou must select at least one character type. Try again.")
    else:
        print(f"\nYour generated password is:\n\n{password}\n")


if __name__ == "__main__":
    main()
