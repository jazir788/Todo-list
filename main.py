todosList = []

while True:
    user_action = input("Type add or show/display or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todosList.append(todo)
        case 'show' | 'display':
            for item in todosList:
                listLength = len(todosList)
        case 'exit':
            break
        case _:
            print('You entered an unknown command')
