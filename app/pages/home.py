import reflex as rx
from app.components.layout import layout
from app.components.publication_card import publication_card
from app.states.content_state import ContentState, Publication, Category


def _hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                "Volume III · Winter Issue · By Mp Kumawat · Educator, Writer, Head of Department",
                class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-8 animate-fade-rise",
            ),
            rx.el.h1(
                rx.el.span("Qualam", class_name="text-[#1f2422]"),
                rx.el.span("-e-", class_name="text-[#b08b3f] italic"),
                rx.el.span("Hayati", class_name="text-[#244a3c]"),
                class_name="font-display text-6xl sm:text-7xl md:text-8xl lg:text-9xl leading-[0.95] tracking-tight mb-6 animate-fade-rise delay-100",
            ),
            rx.el.div(
                "قلمِ حیاتی",
                class_name="font-display text-3xl md:text-4xl text-[#4a4a44] mb-10 animate-fade-rise delay-200",
            ),
            rx.el.div(
                rx.el.span(
                    "A literary journal of essays, fiction, poetry, and quiet correspondence — carried from the classrooms of Rajasthan toward an American literary magazine, and printed in light, delivered by evening.",
                    class_name="font-display italic text-xl md:text-2xl text-[#3a3f3c] leading-relaxed max-w-2xl mx-auto block",
                ),
                class_name="mb-12 animate-fade-rise delay-300",
            ),
            rx.el.div(
                rx.el.a(
                    rx.el.span(
                        "Enter the Journal",
                        class_name="font-mono-caps text-[0.72rem]",
                    ),
                    rx.icon("arrow-right", size=14),
                    href="/publications",
                    class_name="inline-flex items-center gap-3 bg-[#244a3c] text-[#fbf7ec] px-8 py-4 rounded-sm hover:bg-[#1f4033] transition-all duration-500 hover:gap-4",
                ),
                rx.el.a(
                    rx.el.span(
                        "Browse Categories",
                        class_name="font-mono-caps text-[0.72rem]",
                    ),
                    href="/categories",
                    class_name="inline-flex items-center gap-3 border border-[#1f2422] text-[#1f2422] px-8 py-4 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
                ),
                class_name="flex flex-col sm:flex-row items-center justify-center gap-4 animate-fade-rise delay-400",
            ),
            class_name="text-center max-w-4xl mx-auto",
        ),
        class_name="px-6 pt-24 pb-20 md:pt-32 md:pb-28",
    )


def _featured(pub: Publication) -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    "The Featured Piece",
                    class_name="font-mono-caps text-[0.7rem] text-[#b08b3f]",
                ),
                rx.el.div(class_name="flex-1 h-px bg-[#d9cfb6]"),
                class_name="flex items-center gap-6 mb-10",
            ),
            rx.el.a(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                pub["cover_emblem"],
                                size=48,
                                class_name="text-[#244a3c] mb-6",
                            ),
                            rx.el.div(
                                pub["category"],
                                class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-4",
                            ),
                            rx.el.h2(
                                pub["title"],
                                class_name="font-display text-4xl md:text-5xl lg:text-6xl leading-tight text-[#1f2422] mb-4",
                            ),
                            rx.el.p(
                                pub["subtitle"],
                                class_name="font-display italic text-xl md:text-2xl text-[#4a4a44] mb-8",
                            ),
                            rx.el.p(
                                pub["excerpt"],
                                class_name="text-[1.02rem] text-[#3a3f3c] leading-relaxed mb-8 font-serif-body max-w-xl",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    f"By {pub['author']}",
                                    class_name="text-[0.9rem] text-[#2c3330]",
                                ),
                                rx.el.span("·", class_name="text-[#b08b3f]"),
                                rx.el.span(
                                    pub["date"],
                                    class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
                                ),
                                rx.el.span("·", class_name="text-[#b08b3f]"),
                                rx.el.span(
                                    f"{pub['read_minutes']} min read",
                                    class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
                                ),
                                class_name="flex items-center gap-3 mb-8 flex-wrap",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    "Continue Reading",
                                    class_name="font-mono-caps text-[0.72rem] text-[#244a3c] link-refined",
                                ),
                                rx.icon(
                                    "arrow-up-right",
                                    size=16,
                                    class_name="text-[#244a3c]",
                                ),
                                class_name="inline-flex items-center gap-2",
                            ),
                            class_name="p-10 md:p-14",
                        ),
                        class_name="md:col-span-3",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.icon(
                                    pub["cover_emblem"],
                                    size=120,
                                    class_name="text-[#244a3c]/70",
                                ),
                                class_name="absolute inset-0 flex items-center justify-center",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    "№ 01",
                                    class_name="font-display text-6xl md:text-7xl text-[#b08b3f]/80",
                                ),
                                rx.el.div(
                                    "Winter 2025",
                                    class_name="font-mono-caps text-[0.65rem] text-[#fbf7ec]/80 mt-2",
                                ),
                                class_name="absolute bottom-8 right-8 text-right",
                            ),
                            class_name="relative w-full h-full min-h-[320px]",
                        ),
                        class_name="md:col-span-2 bg-[#244a3c] relative overflow-hidden",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-5 paper-card rounded-sm overflow-hidden lit-card",
                ),
                href=f"/read/{pub['slug']}",
                class_name="block animate-fade-rise",
            ),
            class_name="max-w-6xl mx-auto px-6 lg:px-10",
        ),
        class_name="py-20",
    )


def _latest_grid() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Latest Writing",
                        class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-3",
                    ),
                    rx.el.h2(
                        "From the current issue",
                        class_name="font-display text-4xl md:text-5xl text-[#1f2422]",
                    ),
                ),
                rx.el.a(
                    rx.el.span("All publications", class_name="link-refined"),
                    rx.icon("arrow-right", size=14),
                    href="/publications",
                    class_name="hidden md:inline-flex items-center gap-2 font-mono-caps text-[0.72rem] text-[#244a3c]",
                ),
                class_name="flex items-end justify-between mb-12",
            ),
            rx.el.div(
                rx.foreach(
                    ContentState.latest,
                    lambda p: publication_card(p),
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8",
            ),
            class_name="max-w-6xl mx-auto px-6 lg:px-10",
        ),
        class_name="py-16",
    )


def _category_pill(cat: Category) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(cat["emblem"], size=22, class_name="text-[#244a3c] mb-4"),
            rx.el.div(
                cat["name"],
                class_name="font-display text-xl text-[#1f2422] mb-1",
            ),
            rx.el.div(
                cat["urdu"],
                class_name="font-display text-lg text-[#b08b3f] mb-3",
            ),
            rx.el.div(
                f"{cat['count']} pieces",
                class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
            ),
            class_name="paper-card rounded-sm p-6 lit-card h-full",
        ),
        href=f"/categories/{cat['slug']}",
        class_name="block",
    )


def _categories_teaser() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    "The Sections",
                    class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-3",
                ),
                rx.el.h2(
                    "Wander by category",
                    class_name="font-display text-4xl md:text-5xl text-[#1f2422] mb-3",
                ),
                rx.el.p(
                    "Each section is a room; each room, a small light left on.",
                    class_name="font-display italic text-lg text-[#4a4a44]",
                ),
                class_name="text-center mb-14 max-w-2xl mx-auto",
            ),
            rx.el.div(
                rx.foreach(
                    ContentState.categories,
                    lambda c: _category_pill(c),
                ),
                class_name="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 md:gap-6",
            ),
            class_name="max-w-6xl mx-auto px-6 lg:px-10",
        ),
        class_name="py-20",
    )


def _quote_banner() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(class_name="ornament block text-center mb-8"),
            rx.el.blockquote(
                rx.el.p(
                    "Poetry is the spontaneous overflow of powerful feelings.",
                    class_name="font-display italic text-2xl md:text-3xl lg:text-4xl text-[#1f2422] leading-relaxed max-w-3xl mx-auto",
                ),
                rx.el.footer(
                    "— William Wordsworth · a guiding line for Mp Kumawat, educator and writer",
                    class_name="font-mono-caps text-[0.7rem] text-[#6b6558] mt-8",
                ),
                class_name="text-center",
            ),
            class_name="max-w-4xl mx-auto px-6 lg:px-10",
        ),
        class_name="py-24 bg-[#efe7d3]/40",
    )


def home_page() -> rx.Component:
    return layout(
        _hero(),
        _featured(ContentState.featured),
        _quote_banner(),
        _latest_grid(),
        _categories_teaser(),
    )
