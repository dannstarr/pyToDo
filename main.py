todos = []
print("Welcome to your To-Do List!")
print("Type 'add' to add a new todo, 'show' to show your todo's, or enter 'q' to quit.")

while True:
    command = input("Enter a command: ").strip().lower()
    match command:
        case "exit":
            print("Uploading virus... \nPlease wait... \nvirus upload complete")
            break
        case "add":
            todo = input("Enter ToDo item: ")
            todos.append(todo)
            print("Todo added successfully!")
        case "show" | "display":
            if todos:
                print("Your To-Do List:")
                for item in todos:
                    print(item)
            else:
                print("Your To-Do List is empty.")
        case _:
            print("Please enter a valid command")

