import os

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    """Save tasks to the file"""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    """Display tasks with their index and status"""
    if not tasks:
        print("\nYour to-do List is empty!\n")
        return
    print("\nYour to-do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list"""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def complete_task(tasks):
    """Mark a task as completed"""
    display_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to mark as completed: "))
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number -1)
            print(f"Task '{completed_task}' completed and removed from the list.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """Delete a task from the list"""
    display_tasks(tasks)
    try:
        task_number = int(input("\nEnter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """Main function to run the To-Do List App."""
    print("Welcome to the To-Do List App!")
    tasks = load_tasks()
    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice(1-5): ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye! Your tasks are saved.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
