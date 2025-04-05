task=[]
def main():
    print("\nWelcome to TODO TUI")
    print("---------------------")
    
    while True:
        print("---Select The Choice--")
        print("1.Add Task")
        print("2.Show Task")
        print("3.Delete Task")
        print("4.Exit")

        choice = int(input("Enter the Choice: "))
        
        if choice==1:
            Add=input("Enter the task: ").split()       
            task.append(Add)
            print("Task added!")
        elif choice==2:
            for i in range(len(task)):
                print(i+1,task[i])
        elif choice==3:
            index_del=int(input("Enter the task number to delete: "))
            del task[index_del+1]
        elif choice == 4:
                break
        else:
            print("Invalid input")

if __name__=="__main__":
    main()
