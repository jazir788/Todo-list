from modules.functions import get_todos, write_todos
import time
#import functions

now = time.strftime("%d, %b, %Y  %H:%M:%S   ")
while True:
    print("It is", now)
    user_action= input("Type add, show/display, edit, complete  or exit: ").strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()

        write_todos(todo)

        todos.append(todo + '\n')
    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            editedItem = input('What is the new todo item: ')
            todos[number] = editedItem + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo: {todo_to_remove} was removed from the list"
            print(message)
        except ValueError:
            print("Your command is not valid")
    elif user_action.startswith('exit'):
        break
    else:
        print('You entered an unknown command')
