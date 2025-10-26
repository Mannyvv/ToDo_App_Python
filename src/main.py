from nicegui import ui
from pages import HomePage, AppPage


def root():
    # Header
    with ui.header().classes("bg-blue-600 text-white flex justify-start items-center"):
        ui.icon("thumb_up").classes("m-1 text-2xl")
        ui.label("Another ToDo App").classes("text-xl")
    # Nicegui override
    ui.query(".nicegui-content").classes("p-0 m-0")

    # Body Content
    ui.sub_pages({"/": HomePage, "/app": AppPage}).classes(
        "flex flex-column items-center justify-center w-full h-screen "
    )
    # Footer
    with ui.footer().classes("bg-blue-600 text-white flex justify-center"):
        ui.label("© 2024 Manny's ToDo App")


ui.run(root)
