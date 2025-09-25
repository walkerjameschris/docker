from shiny import App, ui, reactive, render
import random
import subprocess

def get_sensors_output():
    try:
        # Run sensors piped to grep Tctl, using shell=True for the pipe
        result = subprocess.run(
            "sensors | grep Tctl",
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        output = result.stdout.strip()
        return output  # This is the whole matching line, e.g. "Tctl: +50.0°C (high = +80.0°C)"
    except subprocess.CalledProcessError as e:
        print(f"Error running sensors grep: {e}")
        return None

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







