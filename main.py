while True:
    user_action= input("Type add, show/display, edit, complete  or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todo.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith('show'):
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        # list comprehension
       # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            with open('todo.txt', 'r') as file:
                todos = file.readlines()

            editedItem = input('What is the new todo item: ')
            todos[number] = editedItem + '\n'

            with open('todo.txt', 'w') as file:
                todos = file.writelines(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todo.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo: {todo_to_remove} was removed from the list"
            print(message)
        except ValueError:
            print("Your command is not valid")
    elif user_action.startswith('exit'):
        break
    else:
        print('You entered an unknown command')
