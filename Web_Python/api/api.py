from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI
from fastapi import FastAPI
from Web_Python.model.Featured import Featured
from Web_Python.model.Live import Live

fastapi_app = FastAPI()

TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()


@fastapi_app.get("/live/{user}")
async def live(user: str) -> Live:
    return TWITCH_API.live(user)


@fastapi_app.get("/featured")
async def featured() -> list[Featured]:
    return SUPABASE_API.featured()