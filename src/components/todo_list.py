from nicegui import ui, app
import uuid
import json


class TodoList:
    def __init__(self):
        self.todo_list: dict = {}
        self.todo_list = self.load_json()
        self.render_todo_list()
        app.on_disconnect(self.save_todos)

    # def add_todo(self, todo_text : str):
    #     self.todo_list.append(todo_text)
    #     self.render_todo_list.refresh()

    def load_json(self):
        with open("todo.json", "r") as file:
            return json.load(file)

    def add_todo(self, todo_text: str):
        id = self.create_uuid()
        self.todo_list[id] = todo_text
        self.render_todo_list.refresh()

    def delete_todo(self, key):
        self.todo_list.pop(key, None)
        self.render_todo_list.refresh()

    @ui.refreshable
    def render_todo_list(self):
        container = (
            ui.list().props("bordered separator").classes("h-1/2 overflow-auto w-1/8")
        )
        with container:
            for key, item in self.todo_list.items():
                with ui.item(item).props("").classes("w-40px"):
                    with ui.item_section().props("side"):
                        ui.icon("delete").on(
                            "click", lambda k=key: self.delete_todo(k)
                        ).classes("cursor-pointer")

    def create_uuid(self):
        random_uuid = uuid.uuid4()
        random_uuid_str = str(random_uuid)
        return random_uuid_str

    def save_todos(self):
        with open("todo.json", "w") as file:
            json.dump(self.todo_list, file)
