from shiny import App, ui, reactive, render
import subprocess

def get_sensors_temp():
    try:
        result = subprocess.run(
            "sensors | grep Tctl",
            shell=True,
            capture_output=True,
            text=True,
            check=True
        )
        # Extract just the temperature number, e.g. +50.0°C
        line = result.stdout.strip()
        # Example line: "Tctl: +50.0°C (high = +80.0°C)"
        temp = line.split()[1] if line else "N/A"
        return temp
    except subprocess.CalledProcessError:
        return "N/A"

def get_nvidia_smi():
    try:
        # Run nvidia-smi to get GPU utilization and temp summary
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=temperature.gpu,utilization.gpu", "--format=csv,noheader,nounits"],
            capture_output=True,
            text=True,
            check=True
        )
        # Output example: "50, 25"
        output = result.stdout.strip()
        if output:
            temp, util = output.split(", ")
            return f"{temp}°C, {util}%"
        return "N/A"
    except subprocess.CalledProcessError:
        return "N/A"

def make_card(title, value, unit="", color="#3498db"):
    """Return a UI box with nice styling."""
    return ui.div(
        ui.h4(title, style="margin-bottom: 5px; color: white;"),
        ui.h2(f"{value} {unit}".strip(), style="margin: 0; color: white;"),
        style=f"""
            background-color: {color};
            padding: 15px;
            border-radius: 8px;
            width: 180px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        """
    )

app_ui = ui.page_fluid(
    ui.h2("Server Readouts", style="margin-bottom: 20px;"),
    ui.row(
        ui.column(
            3,
            ui.output_ui("temp_card")
        ),
        ui.column(
            3,
            ui.output_ui("gpu_card")
        )
    )
)

def server(input, output, session):

    @output
    @render.ui
    def temp_card():
        temp = get_sensors_temp()
        return make_card("CPU Temp", temp, color="#e67e22")

    @output
    @render.ui
    def gpu_card():
        gpu_status = get_nvidia_smi()
        return make_card("GPU Temp / Util", gpu_status, color="#27ae60")

app = App(app_ui, server)
