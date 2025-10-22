from nicegui import ui
from pages.app_page import ToDoApp


def root():
    with ui.header().classes("bg-blue-600 text-white"):
        ui.label("HEADER")
    ui.query(".nicegui-content").classes("p-0 m-0")
    ui.sub_pages({"/": home, "/app": app}).classes(
        "flex flex-col items-center justify-center w-full h-screen"
    )
    with ui.footer().classes("bg-blue-600 text-white"):
        ui.label("FOOTER")


def home():
    with ui.column().classes("items-center justify-center w-full"):
        ui.label("ToDo List App").classes("text-4xl font-bold mb-4")
        ui.button("Get Started", on_click=lambda: ui.navigate.to("/app"))
        ToDoApp()


def app():
    ui.label("This is the app!")


ui.run(root)
