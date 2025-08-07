import reflex as rx
import Web_Python.utils as utils
import Web_Python.routes as rt
import Web_Python.components.nav_bar as nb
import Web_Python.components.footer as ft
import Web_Python.views.header as hd
import Web_Python.views.projects_links as prs
import Web_Python.views.project as pr
import Web_Python.styles.styles as styles


@rx.page(
    route= rt.Routes.PROYECTOS.value,
    title= utils.curso_title,
    description= utils.curso_description,
    image= utils.image
)


def projects() -> rx.Component:
    return rx.box(
        utils.lang(),
        nb.navbar(),
        rx.center(
            rx.vstack(
                hd.header(details=False),
                prs.projects_links(),
                pr.project(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                spacing="8",
                margin_y=styles.Size.MEDIUM.value,
            ),
        ),
        rx.center(
            ft.footer()
        )
    )
