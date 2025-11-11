from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Input

class Menu(App):
    CSS_PATH = "menu.tcss"
    BINDINGS = [("`","toggle_dark","Toggle theme"), ("q","quit","Exit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Играть", id="play")
        yield Button("Выход", id="quit")
        yield Footer()
    
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "play":
            self.compose_add_child(Input("Entername"))
        elif event.button.id == "quit":
            self.exit()