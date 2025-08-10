import reflex as rx
import httpx
import json

async def jsonresponse_to_bool(response):

    if hasattr(response, "body"):
        data = json.loads(response.body.decode())
        return bool(data.get("live", False))
    else:
        return bool(response.get("live", False))


async def get_live_status(user: str) -> bool:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://localhost:8000/live/{user}")
        data = response.json()
        return data.get("live", False)


#COMUN
def lang() -> rx.Component:
    return rx.script("document.documentElement.lang='es'")


image="python-brands-solid-full.svg"


#INDEX
index_title= "Erich Vollenweider | Analista en Computación"
index_description= "Desarrollador de Software"


#CURSOS
project_title= "Erich Vollenweider | Cursos"
project_description= "Cursos de Python"

