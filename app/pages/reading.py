import reflex as rx
from app.components.layout import layout
from app.states.content_state import ContentState
from app.states.reader_prefs_state import ReaderPrefsState


def _paragraph(text: str) -> rx.Component:
    return rx.el.p(text, class_name="whitespace-pre-line")


def _tag_pill(tag: str) -> rx.Component:
    return rx.el.span(
        f"#{tag}",
        class_name="font-mono-caps text-[0.62rem] tracking-wider text-[#244a3c] bg-[#efe7d3] border border-[#d9cfb6] px-2.5 py-1 rounded-full",
    )


def _theme_button(value: str, icon: str, label: str) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, size=14),
        rx.el.span(label, class_name="font-mono-caps text-[0.62rem]"),
        on_click=ReaderPrefsState.set_theme(value),
        class_name=rx.cond(
            ReaderPrefsState.theme == value,
            "inline-flex items-center gap-1.5 bg-[#244a3c] text-[#fbf7ec] px-3 py-1.5 rounded-sm transition-all duration-300",
            "inline-flex items-center gap-1.5 text-[#4a4a44] px-3 py-1.5 rounded-sm hover:text-[#244a3c] transition-all duration-300",
        ),
        aria_label=f"Reader theme {label}",
    )


def _font_button(size: str, label: str) -> rx.Component:
    return rx.el.button(
        label,
        on_click=ReaderPrefsState.set_font_size(size),
        class_name=rx.cond(
            ReaderPrefsState.font_size == size,
            "font-display bg-[#244a3c] text-[#fbf7ec] px-3 py-1.5 rounded-sm transition-all duration-300",
            "font-display text-[#4a4a44] px-3 py-1.5 rounded-sm hover:text-[#244a3c] transition-all duration-300",
        ),
        aria_label=f"Font size {label}",
    )


def _reader_toolbar(pub) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Reader",
                    class_name="font-mono-caps text-[0.6rem] text-[#6b6558] mr-2",
                ),
                _theme_button("light", "sun", "Day"),
                _theme_button("dark", "moon", "Night"),
                class_name="flex items-center gap-1",
            ),
            rx.el.div(class_name="h-6 w-px bg-[#d9cfb6]"),
            rx.el.div(
                rx.el.span(
                    "Type",
                    class_name="font-mono-caps text-[0.6rem] text-[#6b6558] mr-2",
                ),
                _font_button("sm", "A"),
                _font_button("md", "A"),
                _font_button("lg", "A"),
                class_name="flex items-center gap-1 [&>button:nth-child(2)]:text-base [&>button:nth-child(3)]:text-lg [&>button:nth-child(4)]:text-xl",
            ),
            rx.el.div(class_name="h-6 w-px bg-[#d9cfb6]"),
            rx.el.button(
                rx.icon(
                    "bookmark",
                    size=15,
                    class_name=rx.cond(
                        ReaderPrefsState.bookmarks.contains(pub["slug"]),
                        "fill-[#b08b3f] text-[#b08b3f]",
                        "",
                    ),
                ),
                rx.el.span(
                    rx.cond(
                        ReaderPrefsState.bookmarks.contains(pub["slug"]),
                        "Saved",
                        "Save",
                    ),
                    class_name="font-mono-caps text-[0.62rem]",
                ),
                on_click=ReaderPrefsState.toggle_bookmark(pub["slug"]),
                class_name="inline-flex items-center gap-1.5 text-[#4a4a44] px-3 py-1.5 rounded-sm hover:text-[#244a3c] transition-all duration-300",
            ),
            rx.el.button(
                rx.icon("share-2", size=15),
                rx.el.span("Share", class_name="font-mono-caps text-[0.62rem]"),
                on_click=ContentState.share_current,
                class_name="inline-flex items-center gap-1.5 text-[#4a4a44] px-3 py-1.5 rounded-sm hover:text-[#244a3c] transition-all duration-300",
            ),
            class_name="flex flex-wrap items-center gap-2 md:gap-3",
        ),
        class_name="reader-toolbar sticky top-20 z-30 bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-4 py-2.5 mb-10",
    )


def _prev_next_nav() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.cond(
                ContentState.has_prev_article,
                rx.el.a(
                    rx.el.div(
                        rx.icon("arrow-left", size=14),
                        rx.el.span(
                            "Previous",
                            class_name="font-mono-caps text-[0.65rem]",
                        ),
                        class_name="flex items-center gap-2 text-[#b08b3f] mb-3",
                    ),
                    rx.el.div(
                        ContentState.prev_publication["category"],
                        class_name="font-mono-caps text-[0.6rem] text-[#6b6558] mb-1",
                    ),
                    rx.el.h4(
                        ContentState.prev_publication["title"],
                        class_name="font-display text-2xl text-[#1f2422] group-hover:text-[#244a3c] transition-colors",
                    ),
                    href=f"/read/{ContentState.prev_publication['slug']}",
                    class_name="group block paper-card rounded-sm p-6 lit-card h-full",
                ),
                rx.el.div(class_name="h-full"),
            ),
            class_name="h-full",
        ),
        rx.el.div(
            rx.cond(
                ContentState.has_next_article,
                rx.el.a(
                    rx.el.div(
                        rx.el.span(
                            "Next",
                            class_name="font-mono-caps text-[0.65rem]",
                        ),
                        rx.icon("arrow-right", size=14),
                        class_name="flex items-center justify-end gap-2 text-[#b08b3f] mb-3",
                    ),
                    rx.el.div(
                        ContentState.next_publication["category"],
                        class_name="font-mono-caps text-[0.6rem] text-[#6b6558] mb-1 text-right",
                    ),
                    rx.el.h4(
                        ContentState.next_publication["title"],
                        class_name="font-display text-2xl text-[#1f2422] text-right group-hover:text-[#244a3c] transition-colors",
                    ),
                    href=f"/read/{ContentState.next_publication['slug']}",
                    class_name="group block paper-card rounded-sm p-6 lit-card h-full",
                ),
                rx.el.div(class_name="h-full"),
            ),
            class_name="h-full",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 gap-5 mt-16",
    )


def reading_page() -> rx.Component:
    pub = ContentState.current_publication
    return layout(
        rx.el.article(
            rx.el.div(
                rx.el.a(
                    rx.icon("arrow-left", size=14),
                    rx.el.span(
                        "Back to publications", class_name="link-refined"
                    ),
                    href="/publications",
                    class_name="inline-flex items-center gap-2 font-mono-caps text-[0.7rem] text-[#244a3c] mb-8",
                ),
                _reader_toolbar(pub),
                rx.el.header(
                    rx.el.div(
                        rx.el.a(
                            pub["category"],
                            href="/categories",
                            class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] hover:text-[#244a3c] transition-colors",
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
                        class_name="flex items-center gap-3 mb-6 flex-wrap animate-fade-rise",
                    ),
                    rx.el.h1(
                        pub["title"],
                        class_name="font-display text-5xl md:text-6xl lg:text-7xl leading-[1.05] text-[#1f2422] mb-5 animate-fade-rise delay-100",
                    ),
                    rx.el.p(
                        pub["subtitle"],
                        class_name="font-display italic text-xl md:text-2xl text-[#4a4a44] mb-10 animate-fade-rise delay-200",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                pub["cover_emblem"],
                                size=22,
                                class_name="text-[#244a3c]",
                            ),
                            class_name="w-11 h-11 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec]",
                        ),
                        rx.el.div(
                            rx.el.div(
                                pub["author"],
                                class_name="font-display text-lg text-[#1f2422]",
                            ),
                            rx.el.div(
                                "Contributor",
                                class_name="font-mono-caps text-[0.6rem] text-[#6b6558]",
                            ),
                        ),
                        class_name="flex items-center gap-4 mb-12 animate-fade-rise delay-300",
                    ),
                    rx.el.div(class_name="gold-rule mb-14"),
                ),
                rx.cond(
                    pub["cover_image"] != "",
                    rx.el.div(
                        rx.el.img(
                            src=pub["cover_image"],
                            alt=pub["title"],
                            loading="lazy",
                            decoding="async",
                            class_name="w-full max-h-[420px] object-cover rounded-sm border border-[#d9cfb6] mb-14",
                        ),
                        class_name="max-w-3xl mx-auto animate-fade-in",
                    ),
                    rx.fragment(),
                ),
                rx.el.div(
                    rx.cond(
                        pub["body_markdown"] != "",
                        rx.markdown(
                            pub["body_markdown"],
                            class_name="prose-lit prose-markdown animate-fade-in delay-300",
                        ),
                        rx.el.div(
                            rx.el.div(class_name="drop-cap"),
                            rx.foreach(pub["body"], _paragraph),
                            class_name="prose-lit animate-fade-in delay-300",
                        ),
                    ),
                    class_name="max-w-2xl mx-auto",
                ),
                rx.cond(
                    pub["tags"].length() > 0,
                    rx.el.div(
                        rx.el.div(
                            "Tags",
                            class_name="font-mono-caps text-[0.65rem] text-[#6b6558] mb-3",
                        ),
                        rx.el.div(
                            rx.foreach(pub["tags"], _tag_pill),
                            class_name="flex flex-wrap gap-2",
                        ),
                        class_name="max-w-2xl mx-auto mt-14",
                    ),
                    rx.fragment(),
                ),
                rx.el.div(
                    _prev_next_nav(),
                    class_name="max-w-4xl mx-auto",
                ),
                rx.el.div(class_name="thin-rule mt-16"),
                rx.el.div(
                    rx.el.div(class_name="ornament block text-center mb-8"),
                    rx.el.p(
                        "If this piece kept you company, consider wandering into an adjacent room.",
                        class_name="font-display italic text-lg text-[#4a4a44] text-center mb-8",
                    ),
                    rx.el.div(
                        rx.el.a(
                            rx.el.span(
                                "More publications",
                                class_name="font-mono-caps text-[0.72rem]",
                            ),
                            rx.icon("arrow-right", size=14),
                            href="/publications",
                            class_name="inline-flex items-center gap-2 border border-[#1f2422] text-[#1f2422] px-6 py-3 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
                        ),
                        rx.el.a(
                            rx.el.span(
                                "Browse categories",
                                class_name="font-mono-caps text-[0.72rem]",
                            ),
                            href="/categories",
                            class_name="inline-flex items-center gap-2 bg-[#244a3c] text-[#fbf7ec] px-6 py-3 rounded-sm hover:bg-[#1f4033] transition-all duration-500",
                        ),
                        class_name="flex flex-wrap justify-center gap-4",
                    ),
                    class_name="mt-14 max-w-2xl mx-auto",
                ),
                class_name="max-w-4xl mx-auto px-6 lg:px-10",
            ),
            class_name=rx.cond(
                ReaderPrefsState.theme == "dark",
                "reader-dark pt-10 md:pt-16 pb-24 transition-colors duration-500",
                "pt-10 md:pt-16 pb-24 transition-colors duration-500",
            ),
            custom_attrs={
                "data-reader-font": ReaderPrefsState.font_size,
            },
        ),
    )
