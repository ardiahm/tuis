from textual.app import App, ComposeResult

from clock import Clock
from date import Date
from memory import Memory
from cpu import CPU
from disk import Disk
from docker_containers import DockerContainers

from textual.containers import Vertical, Grid

class JarvisApp(App):
    """A Jarvis-Esque dashboard"""

    CSS_PATH = "jarvis01.tcss"


    def compose(self) -> ComposeResult:

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
            

if __name__ == "__main__":
    app = JarvisApp()
    app.run()