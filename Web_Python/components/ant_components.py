import reflex as rx
import Web_Python.styles.colors as color


class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton"
    icon = rx.Var[rx.image()]
    href = rx.Var[str]
    target = "_blank"
    badge = {
        "dot": True,
        "color": color.Color.PRIMARY.value
    }


float_button = FloatButton.create