import os
tasks=[]
def print_list():
    for idx, i in enumerate(tasks[0:5]):
            print(f"{idx + 1}. {i}")
    if len(tasks)>5:
            print("--more--")
    
        
def main():
    
    
    while True:
        print("[1]Add Task [2]Show All Task [3]Delete Task [4]Edit Task [5]Exit")
        choice = int(input("Enter Your Choice: "))
       
               
        if choice == 1: 
            os.system("cls")
            t = input("Enter the task/s:")
            tasks.append(t)
            os.system("cls")
            print_list()

        elif choice == 2:
            os.system("cls")
            for idx, i in enumerate(tasks):
                print(f"{idx + 1}. {i}")
            
        elif choice == 3:
            index_del = int(input("Enter the task number to delete:"))
            del tasks[index_del - 1]

        elif choice == 4:
            n = int(input("Choose task number:")) - 1
            edit = input("Edit: ")
            tasks[n] = edit

        elif choice == 5:
            break

        else:
            print("Invalid input")
if __name__ == "__main__":
    main()
