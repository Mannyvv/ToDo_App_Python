from nicegui import ui


class ToDoApp:
    def __init__(self):
        self.card = self.card_creator()

    def card_creator(self):
        with ui.card():
            ui.label("This is the app")
