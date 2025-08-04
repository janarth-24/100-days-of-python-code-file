import json
import os

# File path for storing tasks
TASK_FILE = "my_task.json"

# Ensure the JSON file exists and is valid
def initialize_task_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as file:
            json.dump([], file)
    else:
        try:
            with open(TASK_FILE, 'r') as file:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError
        except (json.JSONDecodeError, ValueError):
            print("Corrupted task file detected. Resetting it.")
            with open(TASK_FILE, 'w') as file:
                json.dump([], file)

# Load tasks from the JSON file
def load_task():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

# Save tasks to the JSON file
def save_task(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

# View all tasks
def view_task():
    tasks = load_task()
    if tasks:
        print("\n--- Your Tasks ---")
        for idx, task in enumerate(tasks, start=1):
            if isinstance(task, dict) and 'task' in task and 'status' in task:
                print(f"{idx}. {task['task']} - {task['status']}")
            else:
                print(f"{idx}. [Invalid task data]")
        print()
    else:
        print("No tasks found.\n")

# Add a new task
def add_task():
    task_name = input("Enter the task name: ").strip()
    if task_name:
        tasks = load_task()
        tasks.append({"task": task_name, "status": "incomplete"})
        save_task(tasks)
        print(f"Task '{task_name}' added successfully.\n")
    else:
        print("Task name cannot be empty.\n")

# Update the status of a task
def update_task():
    tasks = load_task()
    view_task()
    try:
        index = int(input("Enter the task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_status = input("Enter the status (incomplete/complete): ").strip().lower()
            if new_status in ['incomplete', 'complete']:
                tasks[index]['status'] = new_status
                save_task(tasks)
                print("Task status updated successfully.\n")
            else:
                print("Invalid status. Please use 'incomplete' or 'complete'.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

# Delete a task
def delete_task():
    tasks = load_task()
    view_task()
    try:
        index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            save_task(tasks)
            print(f"Task '{deleted['task']}' deleted successfully.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Invalid input! Please enter a valid number.\n")

# Display the menu
def show_menu():
    print("--- TO-DO Menu ---")
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Update task status")
    print("4. Delete a task")
    print("5. Exit")

# Main program loop
def main():
    initialize_task_file()
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_task()
            elif choice == 3:
                update_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Exiting the To-Do App. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

# Run the app
if __name__ == "__main__":
    main()
