from shiny import App, ui, reactive, render
import random

app_ui = ui.page_fluid(
    ui.card(
        ui.output_text("temp"),
        style="width: 200px; margin-top: 100px"
    )
)

def server(input, output, session):

    def temp():
        return f"CPU Temp: {random.random()}"

app = App(app_ui, server)
