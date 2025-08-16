import reflex as rx
import Web_Python.styles.styles as styles



def link_button_esp(title: str, sub_title: str, url: str, icono: str, is_ext: bool) -> rx.Component:
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
                    rx.text(sub_title, style=styles.button_body_style),
                    align_items="start",
                    spacing="0",
                    padding_right= styles.Size.SMALL.value
                ),
                align="center",
                width="100%"
            ),
        ),
        href=url,
        is_external=is_ext,
        width="100%"
    )
