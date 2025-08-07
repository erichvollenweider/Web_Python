import reflex as rx
import Web_Python.styles.styles as styles



def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size= "8",
        style=styles.title_style,
        padding_x= styles.Size.SMALL.value
    )