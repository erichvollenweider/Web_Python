import reflex as rx
import Web_Python.components.link_button as lb
import Web_Python.components.title as tt
import Web_Python.constants as cte
import Web_Python.routes as rt
import Web_Python.styles.styles as styles

def projects_links() -> rx.Component:
    return rx.vstack(
        lb.link_button("Github", cte.GITHUB, "github", True),
        width="100%"
    )