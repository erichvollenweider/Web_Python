import reflex as rx
import Web_Python.styles.styles as styles
import Web_Python.styles.colors as colors
import Web_Python.routes as rt
import Web_Python.components.ant_components as fb

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.fragment(
                    rx.text("Erich", as_="span", font_weight="bold", color=colors.Color.PRIMARY.value),
                    rx.text("Vollenweider", as_="span", font_weight="bold", color=colors.Color.SECUNDARY.value),
                ),
                style=styles.navbar_title_style
            ),
            href=rt.Routes.INDEX.value
        ),
        fb.float_button(
            icon="python-brands-solid-full.svg",
            href="https://github.com/erichvollenweider"
        ),
        position="sticky",
        bg=colors.Color.CONTENT.value,
        padding_x=styles.Size.LARGE.value,
        padding_y=styles.Size.SMALL.value,
        z_index=999,
        top="0"
    )

