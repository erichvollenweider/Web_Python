import reflex as rx
import Web_Python.utils as utils

class PageState(rx.State):

    is_live: bool = False
    is_title: str = ""

    async def check_live(self):
        live_data=await utils.get_live_status("erich_vollenweider")
        self.is_live = live_data["live"]
        self.is_title = live_data["title"]
