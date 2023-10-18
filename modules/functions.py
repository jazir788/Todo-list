def get_todos(filepath = "todo.txt"):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todo_item, filepath="todo.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todo_item)