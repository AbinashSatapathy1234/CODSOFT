# python
# TO-DO LIST program

todo_list = []

def show_menu():
    print("TO-DO LIST MENU")
    print("1. Show all tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Quit")

def show_tasks():
    print("TO-DO LIST:")
    for i, task in enumerate(todo_list, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ")
    todo_list.append(task)
    print(f"Task '{task}' added!")

def delete_task():
    show_tasks()
    task_number = int(input("Enter the task number to delete: "))
    try:
        del todo_list[task_number - 1]
        print("Task deleted!")
    except IndexError:
        print("Invalid task number!")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again!")