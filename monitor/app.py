from shiny import App, ui, reactive, render
import random
import subprocess

def get_sensors_output():
    try:
        result = subprocess.run(['sensors'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error calling sensors: {e}"

app_ui = ui.page_fluid(
    ui.card(
        ui.output_text("temp"),
        style="width: 200px; margin-top: 100px"
    )
)

def server(input, output, session):

    @output
    @render.text
    def temp():
        return get_sensors_output()
        
app = App(app_ui, server)



