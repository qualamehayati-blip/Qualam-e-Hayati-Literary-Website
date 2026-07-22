import reflex as rx
from app.states.auth_state import AuthState


def _nav_item(
    label: str, href: str, icon: str, active: bool = False
) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, size=15, class_name="text-[#b08b3f]"),
        rx.el.span(label, class_name="link-refined"),
        href=href,
        class_name=rx.cond(
            active,
            "flex items-center gap-3 px-4 py-2.5 rounded-sm font-mono-caps text-[0.68rem] bg-[#244a3c] text-[#fbf7ec]",
            "flex items-center gap-3 px-4 py-2.5 rounded-sm font-mono-caps text-[0.68rem] text-[#2c3330] hover:bg-[#efe7d3]/70 transition-colors duration-500",
        ),
    )


def _sidebar(active: str) -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("feather", size=22, class_name="text-[#244a3c]"),
                    rx.el.div(
                        rx.el.div(
                            "Qualam-e-Hayati",
                            class_name="font-display text-xl text-[#1f2422]",
                        ),
                        rx.el.div(
                            "Editorial Desk",
                            class_name="font-mono-caps text-[0.58rem] text-[#b08b3f] mt-0.5",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="flex items-center gap-3",
                ),
                href="/admin",
                class_name="block",
            ),
            class_name="px-6 py-6 border-b border-[#d9cfb6]",
        ),
        rx.el.nav(
            _nav_item(
                "Dashboard", "/admin", "layout-dashboard", active == "dashboard"
            ),
            _nav_item(
                "New Piece", "/admin/publications/new", "plus", active == "new"
            ),
            _nav_item(
                "Categories",
                "/admin/categories",
                "folder",
                active == "categories",
            ),
            _nav_item("View Journal", "/", "external-link", False),
            class_name="flex flex-col gap-1 p-4",
        ),
        rx.el.div(
            rx.el.div(class_name="thin-rule mb-4"),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "shield-check", size=14, class_name="text-[#244a3c]"
                    ),
                    rx.el.span(
                        "Signed in as admin",
                        class_name="font-mono-caps text-[0.6rem] text-[#6b6558]",
                    ),
                    class_name="flex items-center gap-2 mb-3",
                ),
                rx.el.button(
                    rx.icon("log-out", size=14),
                    rx.el.span(
                        "Sign out",
                        class_name="font-mono-caps text-[0.65rem]",
                    ),
                    on_click=AuthState.logout,
                    class_name="inline-flex items-center gap-2 border border-[#1f2422] text-[#1f2422] px-3 py-2 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500 w-full justify-center",
                ),
                class_name="px-6 pb-6",
            ),
            class_name="mt-auto",
        ),
        class_name="hidden md:flex flex-col w-64 shrink-0 h-screen sticky top-0 bg-[#fbf7ec] border-r border-[#d9cfb6]",
    )


def _mobile_topbar(active: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("feather", size=18, class_name="text-[#244a3c]"),
                rx.el.span(
                    "Editorial Desk",
                    class_name="font-display text-lg text-[#1f2422]",
                ),
                href="/admin",
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("layout-dashboard", size=15),
                    href="/admin",
                    class_name="p-2 rounded-sm text-[#2c3330] hover:bg-[#efe7d3]",
                ),
                rx.el.a(
                    rx.icon("plus", size=15),
                    href="/admin/publications/new",
                    class_name="p-2 rounded-sm text-[#2c3330] hover:bg-[#efe7d3]",
                ),
                rx.el.a(
                    rx.icon("folder", size=15),
                    href="/admin/categories",
                    class_name="p-2 rounded-sm text-[#2c3330] hover:bg-[#efe7d3]",
                ),
                rx.el.button(
                    rx.icon("log-out", size=15),
                    on_click=AuthState.logout,
                    class_name="p-2 rounded-sm text-[#2c3330] hover:bg-[#efe7d3]",
                ),
                class_name="flex items-center gap-1",
            ),
            class_name="flex items-center justify-between px-4 py-3",
        ),
        rx.el.div(class_name="gold-rule opacity-70"),
        class_name="md:hidden bg-[#fbf7ec] border-b border-[#d9cfb6] sticky top-0 z-30",
    )


def admin_layout(*children: rx.Component, active: str = "") -> rx.Component:
    """Layout shell used for every authenticated admin page."""
    return rx.el.div(
        _sidebar(active),
        rx.el.div(
            _mobile_topbar(active),
            rx.el.main(
                rx.el.div(
                    *children,
                    class_name="max-w-6xl mx-auto px-4 md:px-8 py-8 md:py-12",
                ),
                class_name="flex-1",
            ),
            class_name="flex-1 min-h-screen",
        ),
        class_name="flex parchment-bg min-h-screen text-[#1f2422] font-serif-body",
    )
