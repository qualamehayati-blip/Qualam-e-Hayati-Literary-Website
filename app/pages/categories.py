import reflex as rx
from app.components.layout import layout
from app.components.publication_card import publication_card
from app.states.content_state import ContentState, Category


def _category_card(cat: Category) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        cat["emblem"], size=32, class_name="text-[#244a3c]"
                    ),
                    class_name="w-16 h-16 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec]",
                ),
                rx.el.div(
                    cat["urdu"],
                    class_name="font-display text-3xl text-[#b08b3f]",
                ),
                class_name="flex items-center justify-between mb-6",
            ),
            rx.el.h3(
                cat["name"],
                class_name="font-display text-3xl md:text-4xl text-[#1f2422] mb-3",
            ),
            rx.el.p(
                cat["description"],
                class_name="text-[0.98rem] text-[#3a3f3c] leading-relaxed mb-6 font-serif-body",
            ),
            rx.el.div(
                rx.el.div(
                    f"{cat['count']} pieces",
                    class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
                ),
                rx.el.div(
                    rx.el.span(
                        "Explore",
                        class_name="font-mono-caps text-[0.7rem] text-[#244a3c]",
                    ),
                    rx.icon(
                        "arrow-up-right", size=14, class_name="text-[#244a3c]"
                    ),
                    class_name="flex items-center gap-1.5",
                ),
                class_name="flex items-center justify-between pt-6 border-t border-[#e4dcc4]",
            ),
            class_name="paper-card rounded-sm p-8 lit-card h-full",
        ),
        href=f"/categories/{cat['slug']}",
        class_name="block h-full",
    )


def categories_page() -> rx.Component:
    return layout(
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    "Sections",
                    class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-6 animate-fade-rise",
                ),
                rx.el.h1(
                    "Categories",
                    class_name="font-display text-6xl md:text-7xl text-[#1f2422] mb-5 animate-fade-rise delay-100",
                ),
                rx.el.div(
                    class_name="ornament block text-center animate-fade-rise delay-200"
                ),
                rx.el.p(
                    "Five rooms in a small house — each with its own weather.",
                    class_name="font-display italic text-lg md:text-xl text-[#4a4a44] max-w-2xl mx-auto mt-6 animate-fade-rise delay-300",
                ),
                class_name="text-center max-w-3xl mx-auto",
            ),
            class_name="px-6 pt-20 pb-14 md:pt-28",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.foreach(
                        ContentState.categories,
                        lambda c: _category_card(c),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 gap-6 md:gap-8",
                ),
                class_name="max-w-5xl mx-auto px-6 lg:px-10",
            ),
            class_name="pb-24",
        ),
    )


def category_detail_page() -> rx.Component:
    return layout(
        rx.el.section(
            rx.el.div(
                rx.el.a(
                    rx.icon("arrow-left", size=14),
                    rx.el.span("All categories", class_name="link-refined"),
                    href="/categories",
                    class_name="inline-flex items-center gap-2 font-mono-caps text-[0.7rem] text-[#244a3c] mb-10",
                ),
                rx.el.div(
                    ContentState.current_category["urdu"],
                    class_name="font-display text-4xl text-[#b08b3f] mb-2 animate-fade-rise",
                ),
                rx.el.h1(
                    ContentState.current_category["name"],
                    class_name="font-display text-6xl md:text-7xl text-[#1f2422] mb-5 animate-fade-rise delay-100",
                ),
                rx.el.div(
                    class_name="ornament block animate-fade-rise delay-200"
                ),
                rx.el.p(
                    ContentState.current_category["description"],
                    class_name="font-display italic text-lg md:text-xl text-[#4a4a44] max-w-2xl mt-6 animate-fade-rise delay-300",
                ),
                class_name="max-w-5xl mx-auto",
            ),
            class_name="px-6 lg:px-10 pt-20 pb-14 md:pt-28",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.foreach(
                        ContentState.current_category_publications,
                        lambda p: publication_card(p),
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8",
                ),
                class_name="max-w-6xl mx-auto px-6 lg:px-10",
            ),
            class_name="pb-24",
        ),
    )
