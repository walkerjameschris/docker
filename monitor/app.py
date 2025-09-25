import shiny.experimental as x
from shiny import App, ui, render, reactive
import subprocess
import shlex
import time

# Define the UI for the app.
app_ui = ui.page_fluid(
    ui.h2("Terminal Command Runner"),
    ui.p("This app runs a terminal command every 10 seconds and displays the output."),
    ui.output_text("command_output")
)

# Define the server logic.
def server(input, output, session):
    # This reactive value will be updated every 10 seconds.
    # It will trigger the observer below.
    invalidate_counter = reactive.Value(0)

    @reactive.Effect
    def _():
        # Invalidate this effect every 10 seconds.
        reactive.invalidate_later(10)
        # Increment the counter to force a re-evaluation of the next effect.
        invalidate_counter.set(invalidate_counter() + 1)

    # This reactive.Calc will run the command whenever invalidate_counter changes.
    @reactive.Calc
    def run_command():
        # Ensure the calculation is reactive to the invalidation counter.
        invalidate_counter()

        # The command to execute. Use shlex to safely split the command string.
        # This example runs 'ls -la' to list files in the current directory.
        command = "ls -la"
        
        try:
            # Use subprocess.run to execute the command.
            # capture_output=True redirects stdout and stderr.
            # text=True decodes the output as a string.
            # Check=True will raise an exception if the command returns a non-zero exit code.
            result = subprocess.run(shlex.split(command), capture_output=True, text=True, check=True)
            
            # Return the command output.
            return f"Command: {command}\nTimestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n{result.stdout}"
        except subprocess.CalledProcessError as e:
            # Handle cases where the command fails.
            return f"Error running command '{command}': {e.stderr}"
        except FileNotFoundError:
            return f"Error: Command '{shlex.split(command)[0]}' not found."

    # Render the command output in the UI.
    @output
    @render.text
    def command_output():
        # Call the reactive Calc function to get the latest output.
        return run_command()

# Create the Shiny app instance.
app = App(app_ui, server)
