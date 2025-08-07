import reflex as rx
import Web_Python.styles.styles as styles
import Web_Python.components.link_project as lp
import Web_Python.components.title as tt
import Web_Python.constants as cte

def project() -> rx.Component:
    return rx.vstack(
        tt.title("Mis Proyectos"),
        rx.grid(
            lp.link_project(
                "calculator.jpg",
                cte.CALC
            ),
            lp.link_project(
                "f1q&l.jpg",
                cte.FUNO
            ),
            lp.link_project(
                "cwai.jpeg",
                cte.CWAI
            ),
            spacing= "3",
            columns={
                "base": "1",     # 1 columna en pantallas chicas
                "md": "repeat(3, 1fr)",       # 3 columnas desde md
            },
        ),
        width= "100%",
        align_items= "center"
    )