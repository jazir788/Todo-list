todosList = []

while True:
    user_action = input("Type add, show/display, edit  or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todosList.append(todo)
        case 'edit':
            print(todosList)
            number = int(input('Number of the todo to edit: '))
            editedItem = input('What is the new todo item')
            number = number-1
            todosList.__setitem__(number, editedItem)
            print(todosList)
        case 'show' | 'display':
            for item in todosList:
                print(item)
        case 'exit':
            break

        case _:
            print('You entered an unknown command')
