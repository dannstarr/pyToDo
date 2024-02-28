todos = []
print("Welcome to your To-Do List!")
print("Type 'add' to add a new todo, 'show' to show your todo's, or Enter 'q' to quit.")

while True:
    command = input("Enter a command: ").strip()
    if command == 'q':
        print("Uploading virus... \nPlease wait... \nvirus upload complete")
        break
    elif command == "add":
        todo = input("Enter ToDo item: ")
        todos.append(todo)
    elif command == "show":
        for item in todos:
            print(item)
    else:
        print("Please enter a valid command")
