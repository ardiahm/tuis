import psutil

from pathlib import Path

from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.reactive import reactive
from textual.widgets import Static, Label
from textual.widget import Widget


class DiskPercentage(Label):
    """A widget to display current disk usage (percentage)"""
    disk_percent = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.update_disk_percent()
        self.set_interval(1, self.update_disk_percent)

    def update_disk_percent(self) -> None:
        """Method to update disk percentage to current"""
        percent = psutil.disk_usage("/Users/ahmed.1196").percent

        if percent < 25.0:
            color = "$success"
        elif percent < 50.0:
            color = "$warning"
        else:
            color = "$error"

        self.update(f"[{color}]{percent:.1f}%[/{color}]")

    def watch_disk_percent(self, value: float) -> None:
        """Method which is called whenever disk percent's value is changed"""
        self.update(f"{value:.1f}%")

class Disk(Widget):
    """A disk details widget."""

    DEFAULT_CSS = Path(Path(__file__).parent / "disk.tcss").read_text(encoding="utf-8")


    def compose(self) -> ComposeResult:
        with Horizontal(id="disk-content"):
            yield Static("󰋊 : ")
            yield DiskPercentage()
