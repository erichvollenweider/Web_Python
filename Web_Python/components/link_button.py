import reflex as rx
import Web_Python.styles.styles as styles



def link_button(title: str, url: str, icono: str, is_ext: bool) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag=icono,
                    width=styles.Size.MEDIUM.value,
                    height=styles.Size.MEDIUM.value,
                    margin=styles.Size.SMALL.value,
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    align_items="start",
                    padding_y= styles.Size.SMALL.value,
                    padding_right= styles.Size.SMALL.value
                ),
                align="center",
                width="100%"
            ),
        ),
        padding_x= styles.Size.DEFAULT.value,
        href=url,
        is_external=is_ext,
        width="100%"
    )
