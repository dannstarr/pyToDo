def show_todos(todo_list):
    print("Your To-Do List:")
    for index, item in enumerate(todos):
        item = item.strip("\n")
        row = f"{index + 1} - {item}"
        print(row)
      
print("Welcome to your To-Do List!")
print("Type 'add', 'show', 'edit', 'complete', or 'exit' to quit.")

with open("todos.txt", "r") as file:
    todos = file.readlines()

while True:
    command = input("Enter a command: ").strip().lower()
    
    match command:
        case "add":
            todo = input("Enter ToDo item: ") + "\n"
            todos.append(todo)
            with open("todos.txt", "a") as file:
                file.writelines(todo)
            print("New ToDo added successfully!")
        case "show" | "display":
            if todos:
                show_todos(todos)
            else:
                print("Your To-Do List is empty.")
        case "edit":
            if todos:
                show_todos(todos)
            number = int(input("Enter the ToDo number to edit: "))
            number -= 1

            while True:
                confirm = ""
                while confirm.lower() not in ("y", "n"):  # Validate input upfront
                    confirm = input(f"The ToDo you have selected to edit is: {todos[number]}, confirm with 'Y' or cancel with 'N' ")

                if confirm.lower() == "y":
                    todos[number] = input(f"Enter the repl acement for {todos[number]}: ") + "\n"
                    with open("todos.txt", "w") as file:
                        file.writelines(todos)
                    print("Todo successfully edited!")
                    break
                elif confirm.lower() == "n":
                    print("Edit cancelled, no files changed")
                    break
        case "complete":
            if todos:
                show_todos(todos)     
                    
            number = int(input("Which number ToDo would you like to mark as complete?"))
            number -=1
            
            print(f"{todos[number]} successfully marked as complete")
            todos.pop(number)
            with open("todos.txt", "w") as file:
                file.writelines(todos)
        case "exit" | "q":
            print("Exiting program...")
            break
        case _:
            print("Please enter a valid command")
