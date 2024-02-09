def display_menu():
    print("Menu:")
    print("")
    print("1. Add data")
    print("")
    print("2. View data")
    print("")
    print("3.  Exit")
    print("")

def add_data():
    new_name = input("Enter name to add:        ")
    port=input("1. port or 2. new sim :    ")
    if port=="1":
        fro=input("from :     ")
        to=input("To :    ")
        date=input("enter date :    ")
        sim=input("enter sim number :    ")
        new_data=[new_name,port,fro,to,date,sim]
        with open("data.txt", "a") as file:
            file.write(str(new_data) + "\n" )
            print("Data added successfully!")
    elif port=="2":
        
        sim_name=input("enter sim name :    ")
        date=input("enter date :    ")
        sim=input("enter sim number:    ")
        data=[new_name,sim_name,"new sim",date,sim]
        with open("data.txt","a") as file:
            file.write(str(data)+"\n")
            print("data add succesfully")
    else:
        print("invalid input")
    
    
        
    

def view_data():
    with open("data.txt", "r") as file:
        data = file.read()
    print("Data:")
    print(data)

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_data()
        
        elif choice == "2":
            view_data()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()