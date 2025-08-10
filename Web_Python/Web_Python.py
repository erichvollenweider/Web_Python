import reflex as rx
from fastapi import FastAPI
from Web_Python.pages.index import index
from Web_Python.pages.projects import projects
from Web_Python.api.api import live
import Web_Python.styles.styles as styles

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

app._api.add_route("/live/{user}", live)