import os
import json

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for idx, task in enumerate(tasks, start=1):
            status = " [X] " if task['completed'] else " [ ] "
            print(f"{idx}.{status}{task['title']} - {task['description']}")

def add_task(tasks, title, description):
    new_task = {'title': title, 'description': description, 'completed': False}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully.")

def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index - 1]['title']}' marked as completed.")
    else:
        print("Invalid task index.")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Application =====")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to mark as completed: "))
            complete_task(tasks, task_index)
        elif choice == '4':
            display_tasks(tasks)
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
