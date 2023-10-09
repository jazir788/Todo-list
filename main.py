while True:
    user_action = input("Type add, show/display, edit, complete  or exit: ").strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todo.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('todo.txt', 'r')
            todos = file.readlines()
            file.close()

            # list comprehension
           # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            editedItem = input('What is the new todo item')
            number = number-1
            #todosList.__setitem__(number, editedItem)
            #print(todosList)
        case 'complete':
            print('complete')
            #number = int(input("Enter the todo item that is complete: "))
            #todosList.pop(number - 1)
            #print(todosList)
        case 'exit':
            break
        case _:
            print('You entered an unknown command')
