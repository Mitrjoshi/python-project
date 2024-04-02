tasks = []


def add_task(description):
    task = {"description": description, "completed": False}
    tasks.append(task)


def list_tasks():
    for idx, task in enumerate(tasks):
        status = "Done" if task["completed"] else "Pending"
        print(f"{idx + 1}. {task['description']} - {status}")


def mark_task_completed(task_number):
    tasks[task_number - 1]["completed"] = True


def remove_task(task_number):
    del tasks[task_number - 1]


while True:
    command = input("Enter command (add, list, mark, remove, quit): ").lower()
    if command == "add":
        description = input("Enter task description: ")
        add_task(description)
    elif command == "list":
        list_tasks()
    elif command == "mark":
        task_number = int(input("Enter task number to mark as completed: "))
        mark_task_completed(task_number)
    elif command == "remove":
        task_number = int(input("Enter task number to remove: "))
        remove_task(task_number)
    elif command == "quit":
        break
