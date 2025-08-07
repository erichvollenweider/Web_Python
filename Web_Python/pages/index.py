import reflex as rx
import Web_Python.utils as utils
import Web_Python.components.nav_bar as nb
import Web_Python.components.footer as ft
import Web_Python.views.header as hd
import Web_Python.views.index_links as lk
import Web_Python.views.project as pr
import Web_Python.styles.styles as styles


@rx.page(
    title= utils.index_title,
    description= utils.index_description,
    image= utils.image
)


def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        nb.navbar(),
        rx.center(
            rx.vstack(
                hd.header(),
                lk.index_links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                spacing="4",
                margin_y=styles.Size.MEDIUM.value,
            ),
        ),
        rx.center(
            ft.footer()
        )
    )
