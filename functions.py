def get_todos(filepath='files/todos.txt'):
    """Return a list of todo items from a file."""
    with open(filepath, "r") as file:
        todo_items = file.readlines()
    return todo_items

def write_todos(todo_items, filepath='files/todos.txt'):
    """Write a todo list to a text file."""
    with open(filepath, "w") as file:
        file.writelines(todo_items)
print(__name__)
if __name__ == "__main__":
    print("Hello from functions!")