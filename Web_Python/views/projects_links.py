import reflex as rx
import Web_Python.components.link_button as lb
import Web_Python.components.title as tt
import Web_Python.constants as cte
import Web_Python.routes as rt
import Web_Python.styles.styles as styles
import Web_Python.components.featured_link as fl
from Web_Python.model.Featured import Featured


def projects_links(featured: list[Featured]) -> rx.Component:
    return rx.vstack(
        lb.link_button("Github", cte.GITHUB, "github", True),
        rx.cond(
            featured.length() > 0,
            rx.vstack(
                tt.title("Destacados"),
                rx.grid(
                    rx.foreach(
                        featured,
                        fl.featured_link
                    ),
                    columns={
                        "base": "1",     # 1 columna en pantallas chicas
                        "md": "repeat(2, 1fr)",       # 3 columnas desde md
                    },
                    spacing="4"
                ),
                spacing="6"
            )
        ),
        width="100%"
    )