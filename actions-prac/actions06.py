from textual.app import App, ComposeResult
from textual.containers import HorizontalScroll
from textual.reactive import reactive
from textual.widgets import Footer, Placeholder

PAGES_COUNT = 10


class PagesApp(App):
    # BINDINGS = (key, action, label)
    BINDINGS = [
        ("n", "next", "Next"),
        ("p", "previous", "Previous"),
    ]

    # define CSS path
    CSS_PATH = "actions06.tcss"

    # initialize a reactive attribute with a initial value
    # reactive is useful in this case to refresh bindings 
    # and listen for another action
    page_no = reactive(0)

    # setting a horiz. scroll container
        # for page number in pages_count
            # yield a placeholder widget, with text for the page no. and id
    def compose(self) -> ComposeResult:
        with HorizontalScroll(id="page-container"):
            for page_no in range(PAGES_COUNT):
                yield Placeholder(f"Page {page_no}", id=f"page-{page_no}")
        yield Footer()

    # when action_next is called (via bindings)
        # incrememnt page_no, refresh bindings (refresh the footer) ->
        # query_one essentially queries to fetch a created widget, 
        # and outputs it
            # in this case, we yield a placeholder widget for each page number,
            # query_one gets it and outputs it whenever action_next is called
    def action_next(self) -> None:
        self.page_no += 1
        self.refresh_bindings()  
        self.query_one(f"#page-{self.page_no}").scroll_visible()

    # action_previous essentially does the same thing,
    # just decrements page numer
    def action_previous(self) -> None:
        self.page_no -= 1
        self.refresh_bindings()  
        self.query_one(f"#page-{self.page_no}").scroll_visible()

    # check action checks if an action may run. In other words,
    # should we even display Next if we are at the last page? -> No? return False
    # or should we even display Prev. if we are the first page? -> No? return False
    # if neither of these cases, return True 

    def check_action(
        self, action: str, parameters: tuple[object, ...]
    ) -> bool | None:  
        """Check if an action may run."""
        if action == "next" and self.page_no == PAGES_COUNT - 1:
            # returning False doesn't display the footer key, but returning None just grays it out
            return False
        if action == "previous" and self.page_no == 0:
            # returning False doesn't display the footer key, but returning None just grays it out
            return False
        return True
    
    # a big note is, rather than stating self.refresh_bindings() on every reactive variable change 
    # (incrememnt/decrement), we should just initialize the reactive with the bindings=True flag
    # to get around this, and automatically refresh the footer each time:
    # page_no = reactive(0, bindings=True)


if __name__ == "__main__":
    app = PagesApp()
    app.run()