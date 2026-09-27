"""
CODSOFT - Python Programming Internship
Task 1: To-Do List Application

A command-line To-Do List app that lets users:
- Add tasks
- View tasks
- Update (mark as done / edit) tasks
- Delete tasks
- Save/load tasks to/from a file so the list persists between runs
"""

import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    """Load tasks from the JSON data file. Returns a list of task dicts."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_tasks(tasks):
    """Save the current list of tasks to the JSON data file."""
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def display_tasks(tasks):
    """Print all tasks in a numbered, readable format."""
    if not tasks:
        print("\nYour to-do list is empty!\n")
        return

    print("\n----- YOUR TO-DO LIST -----")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")
    print("----------------------------\n")


def add_task(tasks):
    title = input("Enter the new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"Added: '{title}'")
    else:
        print("Task cannot be empty.")


def mark_done(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to mark as done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number.")


def edit_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to edit: "))
        new_title = input("Enter the new task text: ").strip()
        if new_title:
            tasks[num - 1]["title"] = new_title
            save_tasks(tasks)
            print("Task updated!")
        else:
            print("Task cannot be empty.")
    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter the task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: '{removed['title']}'")
    except (ValueError, IndexError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    menu = """
========== TO-DO LIST MENU ==========
1. View tasks
2. Add task
3. Mark task as done
4. Edit task
5. Delete task
6. Exit
======================================
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()
