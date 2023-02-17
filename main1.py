todos = []


while True:
    user_action = input("Type add,exit or show")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo")
            todos.append(todo)
        case "show":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case incorrect_command:
            print("please enter the correct command again")


print("bye")
