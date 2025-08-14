from pydantic import BaseModel


class Featured(BaseModel):
    title: str
    description: str
    image: str
    url: str