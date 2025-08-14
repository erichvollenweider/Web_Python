import reflex as rx
import Web_Python.styles.styles as styles

def link_project(imagen: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            height="170px",
            width="200px",
            border_radius= styles.Size.DEFAULT.value,
            src=imagen
        ),
        href=url,
        is_external=True
    )