from time import monotonic

from textual.app import App, ComposeResult
from clock import Clock
from date import Date
from memory import Memory
from cpu import CPU

from textual.containers import Horizontal, Vertical, Grid
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header

class JarvisApp(App):
    """A Jarvis-Esque dashboard"""

    CSS_PATH = "jarvis01.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "toggle dark mode")
        ]

    def compose(self) -> ComposeResult:
        with Grid(id="dashboard"):
            with Horizontal(id="top-panel"):
                with Vertical(id="clock-date"):
                    yield Clock(id="clock")
                    yield Date(id="date")
            yield Horizontal(id="bottom-left")
            with Horizontal(id="system-info"):
                with Vertical(id="info-stack"):
                    yield Memory(id="memory")
                    yield CPU(id="cpu")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = JarvisApp()
    app.run()