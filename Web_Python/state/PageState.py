import reflex as rx
import Web_Python.utils as utils

class PageState(rx.State):

    is_live: bool = False

    async def check_live(self):
        self.is_live = await utils.get_live_status("erich_vollenweider")
