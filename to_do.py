import os

tasks = []

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def print_list():
    for idx, task in enumerate(tasks[0:5]):
        print(f"{idx + 1}. {task}")
    if len(tasks) > 5:
        print("--more--")

def main():
    load_tasks()
    os.system("cls" if os.name == "nt" else "clear")
    print("📋 Top 5 Tasks:")
    print_list()

    while True:
        print("\n[1] Add Task [2] Show All Tasks [3] Delete Task [4] Edit Task [5] Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        os.system("cls" if os.name == "nt" else "clear")

        if choice == 1:
            t = input("Enter the task: ")
            tasks.append(t)
            save_tasks()
            os.system("cls" if os.name == "nt" else "clear")
            print("📋 Top 5 Tasks:")
            print_list()

        elif choice == 2:
            print("📋 All Tasks:")
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task}")

        elif choice == 3:
            print("📋 All Tasks:")
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task}")
            try:
                index_del = int(input("Enter the task number to delete: "))
                if 1 <= index_del <= len(tasks):
                    del tasks[index_del - 1]
                    save_tasks()
                    print("Task deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input.")

        elif choice == 4:
            print("📋 All Tasks:")
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task}")
            try:
                n = int(input("Choose task number to edit: ")) - 1
                if 0 <= n < len(tasks):
                    edit = input("Edit task: ")
                    tasks[n] = edit
                    save_tasks()
                    print("Task updated.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input.")

        elif choice == 5:
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
