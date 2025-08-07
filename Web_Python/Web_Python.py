import reflex as rx
from Web_Python.pages.index import index
from Web_Python.pages.projects import projects
import Web_Python.styles.styles as styles


class State(rx.State):
    pass

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)


