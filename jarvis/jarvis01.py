from time import monotonic

from pyfiglet import figlet_format

from textual.app import App, ComposeResult
from clock import Clock
from date import Date
from memory import Memory
from cpu import CPU
from disk import Disk
from docker_containers import DockerContainers

from textual.containers import Horizontal, Vertical, Grid
from textual.reactive import reactive
from textual.widgets import Button, Digits, Footer, Header, Static

class JarvisApp(App):
    """A Jarvis-Esque dashboard"""

    CSS_PATH = "jarvis01.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "toggle dark mode")
        ]
    

    

    def compose(self) -> ComposeResult:
        CSS = """
        #ascii-logo-one {
            width: auto;
            height: 10;
            text-wrap: nowrap;
        }
        """

        CSS = """
        #ascii-logo-two {
            width: auto;
            height: auto;
            text-wrap: nowrap;
        }
        """

        hello = figlet_format("Hello : ", font="slant")
        name = figlet_format("Ardi", font="slant")

        with Grid(id="dashboard"):
            with Vertical(id="left-panel"):
                with Vertical(id="clock-date"):
                    yield Clock(id="clock")
                    yield Date(id="date")
                with Vertical(id="sys-info"):
                    yield CPU(id="cpu")
                    yield Memory(id="memory")
                    yield Disk(id="disk")
                with Vertical(id="docker-info"):
                    yield DockerContainers()
            

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

if __name__ == "__main__":
    app = JarvisApp()
    app.run()