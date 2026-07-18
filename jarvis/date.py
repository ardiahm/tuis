from datetime import datetime
from pathlib import Path

from textual.widgets import Label

class Date(Label):
    """A date widget"""

    DEFAULT_CSS = Path(Path(__file__).parent / "date.tcss").read_text(encoding="utf-8")


    def on_mount(self) -> None:
        """Start updating the date after teh widget is mounted"""
        self.update_date()
        self.set_interval(60, self.update_date)

    def update_date(self) -> None:
        """Updates the date widget with the current date"""
        today = datetime.now().strftime("%A, %B %d, %Y")
        self.update(today)
