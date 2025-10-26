from nicegui import ui


class TodoInput:
    def __init__(self):
        self.input_container = self.set_inputtext()
        self.todo_list_add_item_function = None

    def set_todo_list_connector(self, add_item_func):
        self.todo_list_add_item_function = add_item_func

    def validate_text(self, input_string):
        if input_string:
            return True
        else:
            return False

    def send_to_list(self):
        input_text_value = self.input_container.value
        is_valid = self.validate_text(input_text_value)
        if is_valid:
            self.todo_list_add_item_function(input_text_value)
            self.input_container.value = ""
        else:
            ui.notify("Please Enter Text")

    def set_inputtext(self):
        instance_input = ui.input(label="Input Todo Here", placeholder="Start Typing")
        instance_input.on("keydown.enter", self.send_to_list)
        return instance_input
