todosList = []
user_prompt = "Please enter a to do item: "

while True:
    todo = input(user_prompt)
    print(todo.title())
    todosList.append(todo)
