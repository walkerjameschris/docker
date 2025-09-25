from shiny import App, ui, reactive, render
import subprocess

def get_cpu_temp():
    return "1"

app_ui = ui.page_fluid(
    ui.card(
        ui.output_text("temp"),
        style="width: 200px; margin-top: 100px"
    )
)

def server(input, output, session):
    @reactive.Effect
    @reactive.periodic(10)
    def _():
        output.temp = render.text(f"CPU Temp: {get_cpu_temp()}°C")

app = App(app_ui, server)

