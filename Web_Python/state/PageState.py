import reflex as rx
import Web_Python.utils as utils
from Web_Python.api.api import live, featured, schedule
from Web_Python.model.Featured import Featured
from Web_Python.model.Live import Live


USER = "polispol1"
class PageState(rx.State):

    live_status = Live(live=False, title="")
    next_live: str = ""
    featured_info: list[Featured] = []

    async def check_live(self):
        self.live_status = await live(USER)
        if not self.live_status.live:
            self.next_live = utils.next_date(await schedule(), "America/Argentina/Buenos_Aires")
            

    async def featured_links(self):
        data = await featured()
        print(data)
        self.featured_info = await featured()