import os

task = []


def main():
    os.system("clear")
    print("\nWelcome to TODO TUI")
    print("---------------------")

    while True:
        os.system("clear")
        print("---Select The Choice--")
        print("1.Add Task")
        print("2.Show Task")
        print("3.Delete Task")
        print("4.Edit Task")
        print("5.Exit")

        choice = int(input("Enter the Choice: "))

        if choice == 1:
            Add = input("Enter the task: ")
            task.append(Add)
            print("Task added!")
        elif choice == 2:
            for idx, i in enumerate(task):
                print(f"{idx + 1}.{i}")
        elif choice == 3:
            index_del = int(input("Enter the task number to delete: "))
            del task[index_del - 1]
        elif choice == 4:
            edit = int(input("Enter number to edit task :"))
            change = input("Edit: ")
            print("Edited")
        elif choice == 5:
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
