from shiny import App, ui, reactive, render

app_ui = ui.page_fluid(
    ui.card(1)
)

app = App(app_ui, None)
