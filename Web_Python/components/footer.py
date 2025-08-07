import reflex as rx
import datetime as dt
import Web_Python.styles.styles as styles
import Web_Python.constants as cte
import Web_Python.styles.colors as colors

def footer() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="python-brands-solid-full.svg",
            width="25px",
            height="auto"
        ),
        rx.link(f"© {dt.date.today().year} Erich Vollenweider",
                href=cte.GLOBE,
                is_external=True),
        rx.text("All rights reserved."),
        rx.text("Made with Reflex"),
        margin_bottom=styles.Size.DEFAULT.value,
        padding_bottom=styles.Size.DEFAULT.value,
        padding_x= styles.Size.DEFAULT.value,
        color=colors.TextColor.FOOTER.value
    )