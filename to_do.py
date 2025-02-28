def main():
    task=[]

    while True:
        print("\n====To do List===")
        print("1.Add Task")
        print("2.Show Task")
        print("3.Update List")
        print("4.Mark as Done")
        print("5.exit")
        
    choice=int(input("Enter the choice:"))
    
    if choice=="1":
        add = int(input("Add:"))

        for i in range(add):
            task = input("Enter task: ")
            task.append(task)
            print("Task Added.")




