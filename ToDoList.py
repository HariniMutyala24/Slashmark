tasks = []

def show_tasks():
    if not tasks:
        print("Your task list is empty.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["done"] else "Not Completed"
            print(f"{i}. {task['name']} ({status})")

def add_new_task(task_name):
    task = {"name": task_name, "done": False}
    tasks.append(task)
    print(f"Task '{task_name}' has been added to your list.")

def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["done"] = True
        print(f"Task {task_index} marked as completed.")
    else:
        print("Invalid task number. Please provide a valid task number.")

def delete_task(task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Task '{removed_task['name']}' removed from your list.")
    else:
        print("Invalid task number. Please provide a valid task number.")

while True:
    print("\nOptions:")
    print("1. Display task list")
    print("2. Add a new task")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task_name = input("Enter the task: ")
        add_new_task(task_name)
    elif choice == '3':
        show_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        complete_task(task_number)
    elif choice == '4':
        show_tasks()
        task_number = int(input("Enter the task number to remove: "))
        delete_task(task_number)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
