import reflex as rx
import Web_Python.utils as utils
from Web_Python.api.api import live, featured, schedule
from Web_Python.model.Featured import Featured
from Web_Python.model.Live import Live


USER = "auronplay"
class PageState(rx.State):

    timezone = ""
    live_status = Live(live=False, title="")
    next_live: str = ""
    featured_info: list[Featured] = []

    # async def check_live(self):
    #     self.live_status = await live(USER)
    #     if not self.live_status.live:
    #         self.next_live = utils.next_date(await schedule(), "America/Argentina/Buenos_Aires")
            

    # async def featured_links(self):
    #     data = await featured()
    #     print(data)
    #     self.featured_info = await featured()

    async def check_live(self):
        self.live_status = await live(USER)

    async def check_schedule(self):
        if self.timezone == "":
            return rx.call_script(
                utils.LOCAL_TIMEZONE_SCRIPT,
                PageState.update_timezone
            )
        else:
            await self.update_timezone(self.timezone)

    async def update_timezone(self, timezone: str):
        self.timezone = timezone
        self.next_live = utils.next_date(await schedule(), self.timezone)

    async def featured_links(self):
        self.featured_info = await featured()
