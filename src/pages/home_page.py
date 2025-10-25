from nicegui import ui


class HomePage:
    def __init__(self):
        self.card = self.card_creator()

    def card_creator(self):
        with ui.column().classes("items-center justify-center w-full"):
            ui.label("ToDo List App").classes("text-4xl font-bold mb-4")
            ui.button("Get Started", on_click=lambda: ui.navigate.to("/app"))
