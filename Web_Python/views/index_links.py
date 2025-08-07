import reflex as rx
import Web_Python.components.link_button as lb
import Web_Python.components.title as tt
import Web_Python.constants as cte
import Web_Python.routes as rt
import Web_Python.styles.styles as styles

def index_links() -> rx.Component:
    return rx.vstack(
        tt.title("Redes Sociales"),
        lb.link_button("Github", cte.GITHUB, "github", True),
        lb.link_button("LinkedIn", cte.LINKEDIN, "linkedin", True),
        lb.link_button("Instagram", cte.INSTAGRAM, "instagram", True),
        lb.link_button("Web", cte.GLOBE, "globe", True),
        tt.title("Proyectos"),
        lb.link_button("Mis Proyectos", rt.Routes.PROYECTOS.value, "folder-git-2", False),
        width="100%"
    )