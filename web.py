import functions
import streamlit as st

todo_items = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todo_items.append(todo)
    functions.write_todos(todo_items)

st.title("My ToDo App")
st.subheader("This is my to-do app")

for index, todo in enumerate(todo_items):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_items.pop(index)
        functions.write_todos(todo_items)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add a todo item...", key="new_todo", on_change=add_todo)
