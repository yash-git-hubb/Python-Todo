print ("TODO List")


Todo={}

def menu():
    print("Menu:")
    print("1. Create a task")
    print("2. List all task")
    print("3. Mark task as completed")
    print("4. delete a task")
    print("5.EXIT")
    
def create():
    t=input("Name of Task: ")
    Todo[t]=0
 
    
def list():
    for i in Todo:
        print(i)

def complete():
    x= input("Name of TAsk you want to mark complete: ")
    if x in Todo:
        if  Todo[x]==1:
            print("already completed")
        
        else:
            Todo[x]=1
            print(f"{x} marked completed")
def delete():
    x=input("Enter task name you want to delete: ")
    if x in Todo:
        Todo.pop(x)
        print("deleted")
        


while True:
    menu()
    ans = int(input("Select yout choice: "))
    match ans:
        case 1:
            create()
        case 2:
            list()
        case 3:
            complete()
        case 4:
            delete()
        case 5:
            break
