def append_todos(filename):
    with open("filename", "a") as file:
            file.writelines(todo)
    return

def read_todos(filename):
    with open(filename, "r") as file:
        todos = file.readlines()
    return todos

def write_todos(filename):
    with open(filename, "w") as file:
                file.writelines(todos)
    
def show_todos(todo_list):
    print("Your To-Do List:")
    for index, item in enumerate(todos):
        item = item.strip("\n")
        row = f"{index + 1} - {item}"
        print(row)
      
print("Welcome to your To-Do List!")
print("Type 'add', 'show', 'edit', 'complete', or 'exit' to quit.")

todos = read_todos("todos.txt")

while True:
    command = input("Enter a command: ").strip().lower()
    
    if command.startswith("add"):
        todo = command[4:] + "\n"
        todos.append(todo)
        append_todos("todos.txt")
        print("New ToDo added successfully!")
        ################################
    elif command.startswith("show"):
        if todos:
            show_todos(todos)
        else:
            print("Your To-Do List is empty.")
         ###############################   
    elif command.startswith("edit"):
        try:
            if todos:
                show_todos(todos)
            while True:
                number = input(f"Enter the ToDo number to edit 1-{len(todos)}")  # Prompt with valid range
                if number.isdigit():
                    number = int(number) - 1
                    if 0 <= number < len(todos):  # Check for valid index within bounds
                        break
                    else:
                        print(f"Invalid number. Please enter a number between 1 and {len(todos)}")
                else:
                    print("Please enter a valid number.")

            while True:
                confirm = ""
                while confirm.lower() not in ("y", "n"):  # Validate input upfront
                    confirm = input(f"The ToDo you have selected to edit is: {todos[number]}, confirm with 'Y' or cancel with 'N' ")

                if confirm.lower() == "y":
                    todos[number] = input(f"Enter the replacement for {todos[number]}: ") + "\n"
                    write_todos("todos.txt")
                    print("Todo successfully edited!")
                    break
                elif confirm.lower() == "n":
                    print("Edit cancelled, no files changed")
                    break
        except ValueError:
            print("Your command was not valid")
            continue     
           ############################### 
    elif command.startswith("complete"):
        try:
            if todos:
                show_todos(todos)     
                    
            number = int(input("Which number ToDo would you like to mark as complete? "))
            number -=1
            
            print(f"{todos[number]} successfully marked as complete")
            todos.pop(number)
            write_todos("todos.txt")
        except:
            print("You entered an invalid value")
            continue
                ###############################
    elif command.startswith("exit"):
        print("Exiting program...")
        break
    else:
        print("Please enter a valid command")
