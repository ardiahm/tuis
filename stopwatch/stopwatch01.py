from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

class StopwatchApp(App):
    """A Textual app to manage stopwatches."""

    # This would be a whole list of bindings. You can set priority=True flag to create hot-keys on app
    # For example, Ctrl-Q is priority=True so there is always a way to exit the app
    BINDINGS = [("d", "toggle_dark", "toggle dark mode")]

    # This is where the actual UI is constructed. 
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    # An Action method, which always begin with "action_" followed by the name of thier action
    # an action method with the named of "action_set_background" will be called by string "toggle_dark" 
    # as found in BINDINGS
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = StopwatchApp()
    app.run()