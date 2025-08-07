import reflex as rx
import Web_Python.styles.styles as styles



def link_icon(url: str, icon: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon,
            stroke_width=2,
            size=25,
            color=rx.color("cyan", 5)
        ),
        href=url,
        is_external=True
    )