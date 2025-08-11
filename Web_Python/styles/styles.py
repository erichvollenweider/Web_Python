import reflex as rx
from enum import Enum
from .colors import Color as color, TextColor as text_color
from .fonts import Font as Font, FontWeight as FontWeight



# Constants
MAX_WIDTH = "600px"

# Sizes

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "/css/styles.css"

]

class Size(Enum):
    ZERO = "0px !important"
    SMALL="0.5em"
    MSMALL="0.9em"
    DEFAULT="1em"
    MEDIUM="2em"
    LARGE="4em"

# Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": color.BACKGROUND.value,
    rx.heading: {
        "color": text_color.HEADER.value,
        "font_family": Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
        
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "color": text_color.HEADER.value,
        "background_color": color.CONTENT.value,
        "white_space": "normal",
        "justify_content": "start",
        "align_items": "center", 
        "_hover": {
            "bg": color.SECUNDARY.value,
            "cursor": "pointer"
        }
    },

    rx.link: {
        "text_decoration": "none",
        "_hover": {}
    }
}

title_style = dict(
    size="6",
    width="100%",
    padding_top=Size.DEFAULT.value
)

button_title_style = dict(
    font_family= Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=Size.MEDIUM.value,
    color = text_color.HEADER.value
)

button_body_style = dict(
    font_family= Font.DEFAULT.value,
    font_weight= FontWeight.LIGHT.value,
    font_size=Size.DEFAULT.value,
    color = text_color.BODY.value
)

navbar_title_style = dict(
    font_family= Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=Size.MEDIUM.value,
)
