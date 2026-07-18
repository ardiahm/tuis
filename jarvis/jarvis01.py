from time import monotonic

from textual.app import App, ComposeResult
from clock import Clock
from date import Date

from textual.containers import HorizontalGroup, VerticalScroll
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header

class JarvisApp(App):
    """A Jarvis-Esque dashboard"""

    CSS_PATH = "jarvis01.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "toggle dark mode")
        ]

    def compose(self) -> ComposeResult:
        yield Clock(id="clock")
        yield Date(id="date")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = JarvisApp()
    app.run()