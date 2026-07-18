from datetime import datetime
from pathlib import Path

from textual.widgets import Digits

class Clock(Digits):
    """A clock widget"""

    DEFAULT_CSS = Path(Path(__file__).parent / "clock.tcss").read_text(encoding="utf-8")

    def on_mount(self) -> None:
        """Start updating the clock after the widget is mounted."""
        self.update_clock()
        self.set_interval(1, self.update_clock)

    def update_clock(self) -> None:
        """Update the widget with the current time"""
        current_time = datetime.now().strftime("%I:%M %p")
        self.update(current_time)
