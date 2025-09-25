from shiny import App, ui, reactive, render

def get_cpu_temp():
    return "1"  # Replace with actual logic if needed

app_ui = ui.page_fluid(
    ui.card(
        ui.output_text("temp"),
        style="width: 200px; margin-top: 100px"
    )
)

def server(input, output, session):

    def temp():
        return f"CPU Temp: {get_cpu_temp()}°C"

app = App(app_ui, server)

