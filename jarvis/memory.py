import psutil

from pathlib import Path

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Digits, Static, Label
from textual.widget import Widget


class MemoryPercentage(Label):
    """A widget to display actively used memory (percentage)"""
    mem_percent = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.update_mem_percent()
        self.set_interval(1, self.update_mem_percent)

    def update_mem_percent(self) -> None:
        """Method to update memory percentage to current"""
        percent = psutil.virtual_memory().percent

        if percent < 70.0:
            color = "$success"
        elif percent < 80.0:
            color = "$warning"
        else:
            color = "$error"

        self.update(f"[{color}]{percent:.1f}%[/{color}]")

    def watch_mem_percent(self, value: float) -> None:
        """Method which is called whenever mem_percent's value is changed"""
        self.update(f"{value:.1f}%")

class MemoryTotal(Label):
    """A widget to display the total memory (in GB)"""
    memory_total = reactive(0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.update_memory_total()
        self.set_interval(500, self.update_memory_total())

    def update_memory_total(self) -> None:
        self.memory_total = psutil.virtual_memory().total

    def watch_memory_total(self, value: int) -> None:
        mem_in_gb = value / (1024**3)
        self.update(f"{mem_in_gb:.1f} GB")

class Memory(Widget):
    """A memory details widget."""

    DEFAULT_CSS = Path(Path(__file__).parent / "memory.tcss").read_text(encoding="utf-8")


    def compose(self) -> ComposeResult:
        with Horizontal(id="memory-content"):
            yield Static(" : ")
            yield MemoryPercentage()
            yield Static(" of ")
                # yield Static(" with ")
            yield MemoryTotal()
                # yield Static( " available")
