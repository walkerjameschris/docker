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
    @reactive.calc
    @reactive.periodic(10)
    def current_temp():
        return get_cpu_temp()

    @output
    @render.text
    def temp():
        return f"CPU Temp: {current_temp()}°C"

app = App(app_ui, server)
