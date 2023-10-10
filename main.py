while True:
    user_action = input("Type add, show/display, edit, complete  or exit: ").strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            # list comprehension
           # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input('Number of the todo to edit: '))
            number -= 1

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            editedItem = input('What is the new todo item: ')
            todos[number] = editedItem + '\n'

            with open('todo.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'complete':
            number = int(input("Enter the todo item that is complete: "))

            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todo.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo: {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break
        case _:
            print('You entered an unknown command')
