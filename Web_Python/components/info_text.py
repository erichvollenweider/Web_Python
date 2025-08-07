import reflex as rx
import Web_Python.styles.styles as styles
import Web_Python.styles.colors as colors


# def info_text(title: str, body: str) -> rx.Component:
#     return rx.box(
#         rx.text(title, as_="span", font_weight="bold", color="blue"),
#         rx.text(body),
#         font_size="1em"
#     )


def info_text(title: str, body: str) -> rx.Component:
    return rx.text(
        rx.fragment(
            rx.text(title, as_="span", font_weight="bold", color=colors.Color.PRIMARY.value),
            f" {body}",
        ),
        font_size="1em",
        color= colors.TextColor.BODY.value,
    )
