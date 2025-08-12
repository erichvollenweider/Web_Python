from .TwitchAPI import TwitchAPI
from .SupabaseAPI import SupabaseAPI
from fastapi.responses import JSONResponse
from fastapi import Request


TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()


async def live(request: Request):
    user = request.path_params.get("user", "")
    data = TWITCH_API.live(user)
    return JSONResponse(content=data)


async def featured() -> list:
    return SUPABASE_API.featured()