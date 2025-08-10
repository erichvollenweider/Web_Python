from .TwichAPI import TwichAPI
from fastapi.responses import JSONResponse
from fastapi import Request


TWICH_API = TwichAPI()


async def live(request: Request):
    user = request.path_params.get("user", "")
    is_live = TWICH_API.live(user)
    return JSONResponse({"live": is_live})

