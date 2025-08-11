import reflex as rx
import httpx
import json
import Web_Python.api.TwitchAPI as api

async def jsonresponse_to_bool(response):

    if hasattr(response, "body"):
        data = json.loads(response.body.decode())
        return bool(data.get("live", False))
    else:
        return bool(response.get("live", False))



async def get_live_status(user: str) -> dict:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"http://localhost:8000/live/{user}", timeout=5)
            if response.status_code == 200:
                return response.json()
        except httpx.RequestError as e:
            print(f"Error solicitando estado de Twitch: {e}")
        return {"live": False, "title": ""}



#COMUN
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


image="python-brands-solid-full.svg"


#INDEX
index_title= "Erich Vollenweider | Analista en Computación"
index_description= "Desarrollador de Software"


#PROYECTOS
project_title= "Erich Vollenweider | Proyectos"
project_description= "Proyectos"

