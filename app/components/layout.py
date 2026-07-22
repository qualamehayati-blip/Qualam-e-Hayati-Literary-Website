import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer


def layout(*children: rx.Component) -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.main(
            *children,
            class_name="min-h-[60vh]",
        ),
        footer(),
        class_name="parchment-bg min-h-screen text-[#1f2422] font-serif-body",
    )
