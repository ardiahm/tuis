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
        self.mem_percent = psutil.virtual_memory().percent

    def watch_mem_percent(self, value: float) -> None:
        """Method which is called whenever mem_percent's value is changed"""
        self.update(f"{value:.1f}%")

class MemoryAvailable(Label):
    """A widget to display the memory (in GB) available"""
    mem_avail = reactive(0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.update_memory_avail()
        self.set_interval(1, self.update_memory_avail)

    def update_memory_avail(self) -> None:
        self.mem_avail = psutil.virtual_memory().available

    def watch_mem_avail(self, value: int) -> None:
        mem_in_gb = value / (1000**3)
        self.update(f"{mem_in_gb:.1f} GB")

class Memory(Widget):
    """A memory details widget."""

    DEFAULT_CSS = Path(Path(__file__).parent / "memory.tcss").read_text(encoding="utf-8")

    def compose(self) -> ComposeResult:
        with Vertical(id="border"):
            yield Static("------------- MEMORY ------------", id="title")
            with Horizontal(id="memory-content"):
                with Vertical(classes="memory-row"):
                    yield Static("Memory Usage: ")
                    yield Static("Memory Available: ")
                with Vertical(classes="memory-values"):
                    yield MemoryPercentage()
                    yield MemoryAvailable()
            yield Static("---------------------------------", id="footer")
