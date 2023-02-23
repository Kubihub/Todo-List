todos = []


while True:
    user_action = input("Type add,exit or show")
    user_action = user_action.strip()
    match user_action:
        case "add":
            todo = input("Enter a todo")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index}->{item}"
                print(row)
        case "exit":
            break
        case incorrect_command:
            print("please enter the correct command again")


print("bye")
