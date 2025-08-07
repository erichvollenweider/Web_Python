import reflex as rx

config = rx.Config(
    app_name="Web_Python",
    api_url="https://erichvollenweider-web.up.railway.app:8000",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)