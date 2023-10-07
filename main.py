todosList = []
while True:
    user_action = input("Type add, show/display, edit, complete  or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todosList.append(todo)
        case 'complete':
            print(todosList)
            number = int(input("Enter the todo item that is complete: "))
            todosList.pop(number-1)
            print(todosList)
        case 'edit':
            print(todosList)
            number = int(input('Number of the todo to edit: '))
            editedItem = input('What is the new todo item')
            number = number-1
            todosList.__setitem__(number, editedItem)
            print(todosList)
        case 'show' | 'display':
            for index, item in enumerate(todosList):
                row = f"{index+1}-{item}"
                print(row)
        case 'exit':
            break
        case _:
            print('You entered an unknown command')
