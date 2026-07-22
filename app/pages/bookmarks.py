import reflex as rx
from app.components.layout import layout
from app.components.publication_card import publication_card
from app.states.reader_prefs_state import ReaderPrefsState


def _empty_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("bookmark", size=32, class_name="text-[#b08b3f]"),
            class_name="w-16 h-16 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec] mb-6 mx-auto",
        ),
        rx.el.h3(
            "Your reading list is empty.",
            class_name="font-display text-3xl md:text-4xl text-[#1f2422] mb-3",
        ),
        rx.el.p(
            "As you read, tap the small bookmark in the reader — the pieces you save will gather here, waiting like folded letters.",
            class_name="font-display italic text-lg text-[#4a4a44] mb-8 max-w-md mx-auto",
        ),
        rx.el.a(
            rx.el.span(
                "Browse publications",
                class_name="font-mono-caps text-[0.72rem]",
            ),
            rx.icon("arrow-right", size=14),
            href="/publications",
            class_name="inline-flex items-center gap-2 bg-[#244a3c] text-[#fbf7ec] px-6 py-3 rounded-sm hover:bg-[#1f4033] transition-all duration-500",
        ),
        class_name="paper-card rounded-sm p-14 text-center max-w-2xl mx-auto",
    )


def bookmarks_page() -> rx.Component:
    return layout(
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    "Your reading list",
                    class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-6 animate-fade-rise",
                ),
                rx.el.h1(
                    "Bookmarks",
                    class_name="font-display text-6xl md:text-7xl text-[#1f2422] mb-5 animate-fade-rise delay-100",
                ),
                rx.el.div(
                    class_name="ornament block text-center animate-fade-rise delay-200"
                ),
                rx.el.p(
                    "The pieces you have saved, kept quietly in your own drawer of the journal.",
                    class_name="font-display italic text-lg md:text-xl text-[#4a4a44] max-w-2xl mx-auto mt-6 animate-fade-rise delay-300",
                ),
                rx.el.div(
                    rx.el.span(
                        f"{ReaderPrefsState.bookmark_count} saved",
                        class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
                    ),
                    rx.cond(
                        ReaderPrefsState.bookmark_count > 0,
                        rx.el.button(
                            rx.icon("trash-2", size=13),
                            rx.el.span(
                                "Clear all",
                                class_name="font-mono-caps text-[0.65rem]",
                            ),
                            on_click=ReaderPrefsState.clear_bookmarks,
                            class_name="inline-flex items-center gap-1.5 text-[#6b6558] hover:text-[#244a3c] transition-colors",
                        ),
                        rx.fragment(),
                    ),
                    class_name="flex items-center gap-4 justify-center mt-6 animate-fade-rise delay-400",
                ),
                class_name="text-center max-w-3xl mx-auto",
            ),
            class_name="px-6 pt-20 pb-12 md:pt-28",
        ),
        rx.el.section(
            rx.el.div(
                rx.cond(
                    ReaderPrefsState.bookmark_count > 0,
                    rx.el.div(
                        rx.foreach(
                            ReaderPrefsState.bookmarked_publications,
                            lambda p: publication_card(p),
                        ),
                        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8",
                    ),
                    _empty_state(),
                ),
                class_name="max-w-6xl mx-auto px-6 lg:px-10",
            ),
            class_name="pb-24",
        ),
    )
