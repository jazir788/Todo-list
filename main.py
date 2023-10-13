while True:
    user_action= input("Type add, show/display, edit, complete  or exit: ").strip()

    if 'add' in user_action or new in user_action:
        todo = user_action[4:]

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todo.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        # list comprehension
       # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1

        with open('todo.txt', 'r') as file:
            todos = file.readlines()

        editedItem = input('What is the new todo item: ')
        todos[number] = editedItem + '\n'

        with open('todo.txt', 'w') as file:
            todos = file.writelines(todos)
    elif 'complete' in user_action:
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
    elif 'exit' in user_action:
        break
    else:
        print('You entered an unknown command')
