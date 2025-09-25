import subprocess
from shiny import App, ui, reactive, render

def get_sensors_temp():
    try:
        result = subprocess.run(
            "sensors | grep Tctl",
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        line = result.stdout.strip()
        temp = line.split()[1] if line else "N/A"
        return temp
    except subprocess.CalledProcessError:
        return "N/A"

def get_nvidia_temp():
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"],
            capture_output=True,
            text=True,
            check=True
        )
        temp = result.stdout.strip()
        return f"{temp}°C" if temp else "N/A"
    except subprocess.CalledProcessError:
        return "N/A"

def make_card(title, value, unit="", color_class="bg-primary"):
    return ui.div(
        ui.div(
            ui.h5(title, class_="card-title mb-2 text-white"),
            ui.h3(f"{value} {unit}".strip(), class_="card-text text-white"),
            class_="card-body text-center"
        ),
        class_=f"card {color_class} mb-3"
    )

app_ui = ui.page_fluid(
    ui.h2("Server Readouts", class_="mb-4"),
    ui.row(
        ui.column(3, ui.output_ui("temp_card")),
        ui.column(3, ui.output_ui("gpu_card"))
    )
)

def server(input, output, session):

    @output
    @render.ui
    def temp_card():
        temp = get_sensors_temp()
        return make_card("CPU Temp", temp, color_class="bg-warning")

    @output
    @render.ui
    def gpu_card():
        gpu_temp = get_nvidia_temp()
        return make_card("GPU Temp", gpu_temp, color_class="bg-success")

app = App(app_ui, server)
