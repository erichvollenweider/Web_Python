from .TwitchAPI import TwitchAPI
from fastapi.responses import JSONResponse
from fastapi import Request


TWITCH_API = TwitchAPI()


async def live(request: Request):
    user = request.path_params.get("user", "")
    data = TWITCH_API.live(user)
    return JSONResponse(content=data)

