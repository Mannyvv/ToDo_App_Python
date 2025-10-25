from nicegui import ui


class AppPage:
    def __init__(self):
        self.card = self.card_creator()
        self.dfd = ui.label("dfdf")

    def card_creator(self):
        with ui.card():
            ui.label("This is the app")
