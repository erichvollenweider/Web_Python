import reflex as rx
import Web_Python.utils as utils
from Web_Python.api.api import live, featured
from Web_Python.model.Featured import Featured
from Web_Python.model.Live import Live


USER = "erich_vollenweider"
class PageState(rx.State):

    live_status = Live(live=False, title="")
    featured_info: list[Featured] = []

    async def check_live(self):
        self.live_status = await live(USER)


    async def featured_links(self):
        data = await featured()
        print(data)
        self.featured_info = await featured()