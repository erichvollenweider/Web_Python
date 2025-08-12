import reflex as rx
import Web_Python.utils as utils
import Web_Python.api.api as api

class PageState(rx.State):

    is_live: bool = False
    is_title: str = ""
    featured_info: list = []

    async def check_live(self):
        live_data=await utils.get_live_status("erich_vollenweider")
        self.is_live = live_data["live"]
        self.is_title = live_data["title"]


    async def featured_links(self):
        self.featured_info = await api.featured()