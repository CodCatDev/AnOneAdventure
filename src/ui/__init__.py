from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Label

class Game(App):
    #CSS_PATH = "game.tcss"
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

class Menu(App):

    text = """           _                                           
  /\\  ._  / \\ ._   _   /\\   _|     _  ._ _|_     ._ _  
 /--\\ | | \\_/ | | (/_ /--\\ (_| \\/ (/_ | | |_ |_| | (/_ 
                                                       """

    TITLE = "AnOneAdventure"
    CSS_PATH = "menu.tcss"
    BINDINGS = [("`","toggle_dark","Toggle theme"), ("q","quit","Exit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label(f" {self.text}", id="title")
        yield Button("Играть", id="play")
        yield Button("Выход", id="quit")
        yield Footer()
    
    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "play":
            self.mount()
        elif event.button.id == "quit":
            self.exit()