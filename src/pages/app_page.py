from components import TodoList, TodoInput


class AppPage:
    def __init__(self):
        self.todo_input, self.todo_list = self.setup_components()

    def setup_components(self):
        todo_input = TodoInput()
        todo_list = TodoList()
        self.bind_input_to_list(todo_input, todo_list)
        return todo_input, todo_list

    def bind_input_to_list(self, todo_input: TodoInput, todo_list: TodoList):
        todo_input.set_todo_list_connector(todo_list.add_todo)
