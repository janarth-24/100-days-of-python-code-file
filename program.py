# Notes Taking App

import datetime

# Define file name
FILE_NAME = "mynotes.txt"

# Display menu options
def show_menu():
    print("\n--- Note-Taking App Menu ---")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Delete all notes")
    print("4. Exit")

# Add a note with a timestamp
def add_notes():
    note = input("Enter your note: ")
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open(FILE_NAME, "a") as file:
        file.write(f"{timestamp} - {note}\n")
    print("Note added successfully.")

# View all notes
def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content:
                print("\n---- Your Notes ----")
                print(content)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")

# Delete all notes
def delete_notes():
    choice = input("Are you sure you want to delete all notes (yes/no): ")
    if choice.lower() == "yes":
        with open(FILE_NAME, "w"):
            pass
        print("All notes have been deleted.")
    else:
        print("Deletion cancelled.")

# Main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_notes()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("Exiting Note-Taking App. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
