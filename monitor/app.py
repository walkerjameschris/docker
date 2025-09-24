from shiny import App, render, ui

# 1. Define the user interface (UI)
app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "Number of values", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)

# 2. Define the server logic
def server(input, output, session):
    @render.text
    def txt():
        return f"The number is {input.n()}"

# 3. Create the Shiny app object
app = App(app_ui, server)
