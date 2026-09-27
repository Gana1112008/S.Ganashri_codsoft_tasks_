"""
CODSOFT - Python Programming Internship
Task 5: Contact Book

A command-line contact management app supporting:
- Add contact (name, phone, email, address)
- View all contacts
- Search contact by name or phone number
- Update contact
- Delete contact
Contacts are saved to a JSON file so they persist between runs.
"""

import json
import os

DATA_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_contacts(contacts):
    with open(DATA_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def display_contact(contact, index=None):
    prefix = f"{index}. " if index is not None else ""
    print(f"{prefix}Name: {contact['name']}")
    print(f"    Phone:   {contact['phone']}")
    print(f"    Email:   {contact.get('email', '-')}")
    print(f"    Address: {contact.get('address', '-')}")


def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts saved yet.\n")
        return
    print("\n----- CONTACT LIST -----")
    for i, contact in enumerate(contacts, start=1):
        display_contact(contact, i)
        print()
    print("-------------------------\n")


def add_contact(contacts):
    print("\nEnter contact details:")
    name = input("Name: ").strip()
    if not name:
        print("Name is required. Contact not added.")
        return
    phone = input("Phone: ").strip()
    email = input("Email (optional): ").strip()
    address = input("Address (optional): ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address,
    })
    save_contacts(contacts)
    print(f"Contact '{name}' added.")


def search_contacts(contacts):
    query = input("\nEnter a name or phone number to search: ").strip().lower()
    results = [
        c for c in contacts
        if query in c["name"].lower() or query in c["phone"]
    ]

    if not results:
        print("No matching contacts found.\n")
        return

    print(f"\nFound {len(results)} matching contact(s):")
    for i, contact in enumerate(results, start=1):
        display_contact(contact, i)
        print()


def find_contact_index(contacts):
    """Helper: show the list, ask for a number, return its index or None."""
    view_contacts(contacts)
    if not contacts:
        return None
    try:
        num = int(input("Enter the contact number: "))
        if 1 <= num <= len(contacts):
            return num - 1
        print("Invalid contact number.")
        return None
    except ValueError:
        print("Please enter a valid number.")
        return None


def update_contact(contacts):
    index = find_contact_index(contacts)
    if index is None:
        return

    contact = contacts[index]
    print("Leave a field blank to keep its current value.")

    name = input(f"Name [{contact['name']}]: ").strip()
    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact.get('email', '-')}]: ").strip()
    address = input(f"Address [{contact.get('address', '-')}]: ").strip()

    if name:
        contact["name"] = name
    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email
    if address:
        contact["address"] = address

    save_contacts(contacts)
    print("Contact updated.")


def delete_contact(contacts):
    index = find_contact_index(contacts)
    if index is None:
        return

    removed = contacts.pop(index)
    save_contacts(contacts)
    print(f"Deleted contact '{removed['name']}'.")


def main():
    contacts = load_contacts()

    menu = """
========== CONTACT BOOK MENU ==========
1. View all contacts
2. Add contact
3. Search contact
4. Update contact
5. Delete contact
6. Exit
=========================================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye! Your contacts have been saved.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
