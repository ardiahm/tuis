import psutil

from pathlib import Path

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Digits, Static, Label
from textual.widget import Widget

# CPU Usage = cpu_percent
# Clock Speed = cpu_stats.cpu_freq

class CPU_Percentage(Label):
    """A widget to display CPU Usage (percentage)"""

    cpu_percent = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added."""
        self.update_cpu_percent()
        self.set_interval(1, self.update_cpu_percent)
    
    def update_cpu_percent(self) -> None:
        """Method to update cpu percentage to current snapshot. """
        self.cpu_percent = psutil.cpu_percent()

    def watch_cpu_percent(self, value: float) -> None:
        """Method which is called whenver cpu_percent's value is changed"""
        self.update(f"{value:.1f}%")
    
class CPU_Speed(Label):
    """A widget to display CPU Speed (GHz)"""

    cpu_speed = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added."""
        self.update_cpu_speed()
        self.set_interval(1, self.update_cpu_speed)
    
    def update_cpu_speed(self) -> None:
        """Method to update cpu speed to current snapshot. """
        self.cpu_speed = (psutil.cpu_freq().current / 1000)

    def watch_cpu_speed(self, value: float) -> None:
        """Method which is called whenver cpu_speed's value is changed"""
        self.update(f"{value:.2f} GHz")

class CPU(Widget):
    """A CPU details widget"""

    DEFAULT_CSS = Path(Path(__file__).parent / "cpu.tcss").read_text(encoding="utf-8")

    def compose(self) -> ComposeResult:
        with Vertical(id="border"):
            yield Static("---------- PROCESSOR -----------", id="title")
            with Horizontal(id="cpu-content"):
                with Vertical(classes="cpu-row"):
                    yield Static("CPU Usage: ")
                    yield Static("CPU Speed: ")
                with Vertical(classes="cpu-values"):
                    yield CPU_Percentage()
                    yield CPU_Speed()
            yield Static("------------------------------", id="footer")
