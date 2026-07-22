import reflex as rx
from app.states.nav_state import NavState
from app.states.reader_prefs_state import ReaderPrefsState


def _nav_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.el.span(label, class_name="link-refined"),
        href=href,
        class_name="font-mono-caps text-[0.72rem] text-[#2c3330] hover:text-[#244a3c] transition-colors duration-500",
    )


def _mobile_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        label,
        href=href,
        on_click=NavState.close_mobile,
        class_name="block font-display text-2xl text-[#1f2422] hover:text-[#244a3c] py-3 border-b border-[#d9cfb6] transition-colors duration-500",
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("feather", size=22, class_name="text-[#244a3c]"),
                    rx.el.div(
                        rx.el.div(
                            "Qualam-e-Hayati",
                            class_name="font-display text-xl sm:text-2xl leading-none text-[#1f2422] tracking-wide",
                        ),
                        rx.el.div(
                            "قلمِ حیاتی  ·  A Literary Journal",
                            class_name="font-mono-caps text-[0.6rem] text-[#6b6558] mt-1",
                        ),
                        class_name="flex flex-col",
                    ),
                    class_name="flex items-center gap-3",
                ),
                href="/",
                class_name="flex items-center",
            ),
            rx.el.nav(
                _nav_link("Home", "/"),
                _nav_link("Publications", "/publications"),
                _nav_link("Categories", "/categories"),
                _nav_link("About", "/about"),
                _nav_link("Contact", "/contact"),
                class_name="hidden md:flex items-center gap-8",
            ),
            rx.el.a(
                rx.icon("bookmark", size=15, class_name="text-[#244a3c]"),
                rx.cond(
                    ReaderPrefsState.bookmark_count > 0,
                    rx.el.span(
                        ReaderPrefsState.bookmark_count,
                        class_name="font-mono-caps text-[0.6rem] bg-[#244a3c] text-[#fbf7ec] rounded-full px-1.5 py-0.5 min-w-[18px] text-center",
                    ),
                    rx.fragment(),
                ),
                href="/bookmarks",
                class_name="hidden md:inline-flex items-center gap-2 border border-[#d9cfb6] rounded-full px-3 py-1.5 hover:border-[#b08b3f] transition-all duration-500",
                aria_label="Reading list",
            ),
            rx.el.button(
                rx.icon(
                    rx.cond(NavState.mobile_open, "x", "menu"),
                    size=22,
                    class_name="text-[#1f2422]",
                ),
                on_click=NavState.toggle_mobile,
                class_name="md:hidden p-2 rounded-full hover:bg-[#efe7d3] transition-colors",
                aria_label="Open menu",
            ),
            class_name="max-w-6xl mx-auto px-6 lg:px-10 h-20 flex items-center justify-between",
        ),
        rx.el.div(class_name="gold-rule opacity-70"),
        rx.cond(
            NavState.mobile_open,
            rx.el.div(
                rx.el.div(
                    _mobile_link("Home", "/"),
                    _mobile_link("Publications", "/publications"),
                    _mobile_link("Categories", "/categories"),
                    _mobile_link("Bookmarks", "/bookmarks"),
                    _mobile_link("Feed", "/feed"),
                    _mobile_link("About", "/about"),
                    _mobile_link("Contact", "/contact"),
                    class_name="px-6 py-6 max-w-6xl mx-auto",
                ),
                class_name="md:hidden bg-[#fbf7ec] border-b border-[#d9cfb6] animate-fade-in",
            ),
            rx.fragment(),
        ),
        class_name="sticky top-0 z-40 bg-[#f6f1e4]",
    )
