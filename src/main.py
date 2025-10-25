from nicegui import ui
from pages import HomePage, AppPage


def root():
    # Header
    with ui.header().classes("bg-blue-600 text-white"):
        ui.label("HEADER")
    # Nicegui override
    ui.query(".nicegui-content").classes("p-0 m-0")

    # Body Content
    ui.sub_pages({"/": HomePage, "/app": AppPage}).classes(
        "flex flex-col items-center justify-center w-full h-screen"
    )
    # Footer
    with ui.footer().classes("bg-blue-600 text-white"):
        ui.label("FOOTER")


ui.run(root)
