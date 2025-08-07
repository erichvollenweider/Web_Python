import reflex as rx
import Web_Python.styles.styles as styles
import Web_Python.components.link_icon as icon
import Web_Python.components.info_text as it
import Web_Python.constants as cte
import Web_Python.styles.colors as color


def header(details = True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                #fallback="EV",
                name="Erich Vollenweider",
                src="profile3.png",
                size="7",
                color=color.TextColor.BODY.value,
                bg=color.Color.CONTENT.value,
                border_radius="100%",
                border="4px solid",
                border_color=color.Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.heading(
                    "Erich Vollenweider",
                    size="8"
                ),
                rx.text(
                    "Analista en Computación",
                    color=color.TextColor.BODY.value
                ),
                rx.hstack(
                    icon.link_icon(cte.GITHUB, "github"),
                    icon.link_icon(cte.LINKEDIN, "linkedin"),
                    icon.link_icon(cte.INSTAGRAM, "instagram"),
                    icon.link_icon(cte.GLOBE, "globe")
                ),
                spacing="0",
                align_items="start",
            ),
            align_items="center",
            spacing="4"
        ),
        
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    it.info_text(
                        "+2",
                        "Años de exp."
                    ),
                    rx.spacer(),
                    it.info_text(
                        "+2",
                        "Años de exp."
                    ),
                    rx.spacer(),
                    it.info_text(
                        "+2",
                        "Años de exp."
                    ),
                    width="100%"
                ),

                
                rx.text(
                    f"""
                    Soy Analista en Computación recibido y estudiante de la Licenciatura en Ciencias de la 
                    Computación (cursando 4º año). Tengo conocimientos intermedios de inglés y una fuerte orientación
                    hacia la resolución de problemas, el desarrollo de software y la tecnología. Me interesa el 
                    desarrollo web, la inteligencia artificial, la programación funcional y la programación orientada a objetos.
                    """,
                    color = color.TextColor.BODY.value
                ),
                spacing= "6"
            ),
        ),
        padding_x= styles.Size.DEFAULT.value,
        text_align="justify",
        align_items="start",
        spacing= "6"
    )