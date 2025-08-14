import reflex as rx
import Web_Python.styles.styles as st
from Web_Python.model.Featured import Featured


def featured_link(featured: Featured) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(
                src=featured.image,
                border_radius=st.Size.DEFAULT.value
            ),
            rx.text(
                featured.title,
                style=st.button_title_style
            ),
            rx.text(
                featured.description,
                style=st.button_body_style,
                text_align="justify",
            ),
            spacing="2"
        ),
        href=featured.url,
        is_external= True
    )