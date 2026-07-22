import reflex as rx
from app.components.layout import layout
from app.states.content_state import ContentState, Publication


def _feed_row(pub: Publication) -> rx.Component:
    return rx.el.li(
        rx.el.a(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        pub["date"],
                        class_name="font-mono-caps text-[0.62rem] text-[#6b6558] tracking-wider",
                    ),
                    rx.el.span("·", class_name="text-[#b08b3f]"),
                    rx.el.span(
                        pub["category"],
                        class_name="font-mono-caps text-[0.62rem] text-[#b08b3f]",
                    ),
                    rx.el.span("·", class_name="text-[#b08b3f]"),
                    rx.el.span(
                        f"{pub['read_minutes']} min",
                        class_name="font-mono-caps text-[0.62rem] text-[#6b6558]",
                    ),
                    class_name="flex items-center gap-3 mb-2 flex-wrap",
                ),
                rx.el.h3(
                    pub["title"],
                    class_name="font-display text-2xl md:text-3xl text-[#1f2422] leading-snug group-hover:text-[#244a3c] transition-colors duration-500",
                ),
                rx.el.p(
                    pub["subtitle"],
                    class_name="font-display italic text-[#4a4a44] mt-1",
                ),
                rx.el.p(
                    pub["excerpt"],
                    class_name="text-[0.95rem] text-[#3a3f3c] leading-relaxed mt-3 font-serif-body line-clamp-2",
                ),
                rx.el.div(
                    rx.el.span(
                        f"By {pub['author']}",
                        class_name="text-[0.85rem] text-[#2c3330]",
                    ),
                    rx.icon(
                        "arrow-up-right", size=14, class_name="text-[#244a3c]"
                    ),
                    class_name="flex items-center justify-between mt-4",
                ),
                class_name="py-6",
            ),
            href=f"/read/{pub['slug']}",
            class_name="group block",
        ),
        class_name="border-b border-[#e4dcc4] last:border-b-0",
    )


def feed_page() -> rx.Component:
    return layout(
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    "Feed & Sitemap",
                    class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-6 animate-fade-rise",
                ),
                rx.el.h1(
                    "The Full Ledger",
                    class_name="font-display text-6xl md:text-7xl text-[#1f2422] mb-5 animate-fade-rise delay-100",
                ),
                rx.el.div(
                    class_name="ornament block text-center animate-fade-rise delay-200"
                ),
                rx.el.p(
                    "Every published piece, in chronological order — a plain, patient list for readers, feed readers, and index-makers.",
                    class_name="font-display italic text-lg md:text-xl text-[#4a4a44] max-w-2xl mx-auto mt-6 animate-fade-rise delay-300",
                ),
                class_name="text-center max-w-3xl mx-auto",
            ),
            class_name="px-6 pt-20 pb-12 md:pt-28",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                "Publications",
                                class_name="font-display text-3xl text-[#1f2422]",
                            ),
                            rx.el.div(
                                f"{ContentState.publications.length()} pieces",
                                class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
                            ),
                            class_name="flex items-baseline justify-between mb-2",
                        ),
                        rx.el.p(
                            "Chronological listing of every essay, story, poem, letter, and interview.",
                            class_name="font-display italic text-[#4a4a44] mb-6",
                        ),
                        rx.el.ol(
                            rx.foreach(
                                ContentState.publications,
                                lambda p: _feed_row(p),
                            ),
                        ),
                        class_name="paper-card rounded-sm p-8 md:p-10",
                    ),
                    class_name="lg:col-span-2",
                ),
                rx.el.aside(
                    rx.el.div(
                        rx.el.div(
                            "Sitemap",
                            class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-4",
                        ),
                        rx.el.ul(
                            rx.el.li(
                                rx.el.a(
                                    "Home",
                                    href="/",
                                    class_name="link-refined text-[#2c3330]",
                                ),
                                class_name="mb-2",
                            ),
                            rx.el.li(
                                rx.el.a(
                                    "Publications",
                                    href="/publications",
                                    class_name="link-refined text-[#2c3330]",
                                ),
                                class_name="mb-2",
                            ),
                            rx.el.li(
                                rx.el.a(
                                    "Categories",
                                    href="/categories",
                                    class_name="link-refined text-[#2c3330]",
                                ),
                                class_name="mb-2",
                            ),
                            rx.el.li(
                                rx.el.a(
                                    "Bookmarks",
                                    href="/bookmarks",
                                    class_name="link-refined text-[#2c3330]",
                                ),
                                class_name="mb-2",
                            ),
                            rx.el.li(
                                rx.el.a(
                                    "About",
                                    href="/about",
                                    class_name="link-refined text-[#2c3330]",
                                ),
                                class_name="mb-2",
                            ),
                            rx.el.li(
                                rx.el.a(
                                    "Contact",
                                    href="/contact",
                                    class_name="link-refined text-[#2c3330]",
                                ),
                            ),
                            class_name="font-serif-body text-[0.95rem]",
                        ),
                        class_name="mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            "Sections",
                            class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-4",
                        ),
                        rx.el.ul(
                            rx.foreach(
                                ContentState.categories,
                                lambda c: rx.el.li(
                                    rx.el.a(
                                        rx.el.span(
                                            c["name"], class_name="link-refined"
                                        ),
                                        rx.el.span(
                                            f" · {c['count']}",
                                            class_name="text-[#6b6558]",
                                        ),
                                        href=f"/categories/{c['slug']}",
                                        class_name="text-[#2c3330] font-serif-body text-[0.95rem]",
                                    ),
                                    class_name="mb-2",
                                ),
                            ),
                        ),
                        class_name="mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            "Subscribe",
                            class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-3",
                        ),
                        rx.el.p(
                            "This page serves as our reader-facing feed. Point your feed reader here — new pieces will appear at the top.",
                            class_name="text-[0.9rem] text-[#4a4a44] leading-relaxed font-serif-body mb-4",
                        ),
                        rx.el.a(
                            rx.icon("rss", size=14),
                            rx.el.span(
                                "Follow the feed",
                                class_name="font-mono-caps text-[0.7rem]",
                            ),
                            href="/feed",
                            class_name="inline-flex items-center gap-2 border border-[#1f2422] text-[#1f2422] px-4 py-2.5 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
                        ),
                        class_name="",
                    ),
                    class_name="paper-card rounded-sm p-8 h-fit lg:sticky lg:top-28",
                ),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-8",
            ),
            class_name="max-w-6xl mx-auto px-6 lg:px-10 pb-24",
        ),
    )
