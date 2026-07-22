import reflex as rx
from app.states.content_state import Publication


def publication_card(pub: Publication) -> rx.Component:
    return rx.el.a(
        rx.el.article(
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        pub["cover_emblem"],
                        size=28,
                        class_name="text-[#244a3c]",
                    ),
                    class_name="w-14 h-14 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec]",
                ),
                rx.el.div(
                    rx.el.div(
                        pub["category"],
                        class_name="font-mono-caps text-[0.65rem] text-[#b08b3f]",
                    ),
                    rx.el.div(
                        pub["date"],
                        class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
                    ),
                    class_name="flex flex-col items-end gap-1",
                ),
                class_name="flex items-start justify-between mb-6",
            ),
            rx.el.h3(
                pub["title"],
                class_name="font-display text-2xl md:text-[1.65rem] text-[#1f2422] leading-tight mb-2",
            ),
            rx.el.p(
                pub["subtitle"],
                class_name="font-display italic text-[#4a4a44] text-lg mb-5",
            ),
            rx.el.p(
                pub["excerpt"],
                class_name="text-[0.98rem] text-[#3a3f3c] leading-relaxed mb-6 font-serif-body line-clamp-3",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        pub["author"],
                        class_name="text-[0.85rem] text-[#2c3330]",
                    ),
                    rx.el.span("·", class_name="text-[#b08b3f]"),
                    rx.el.span(
                        f"{pub['read_minutes']} min read",
                        class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
                    ),
                    class_name="flex items-center gap-3",
                ),
                rx.el.div(
                    rx.el.span(
                        "Read",
                        class_name="font-mono-caps text-[0.7rem] text-[#244a3c]",
                    ),
                    rx.icon(
                        "arrow-up-right", size=14, class_name="text-[#244a3c]"
                    ),
                    class_name="flex items-center gap-1.5",
                ),
                class_name="flex items-center justify-between pt-5 border-t border-[#e4dcc4]",
            ),
            class_name="paper-card rounded-sm p-7 md:p-8 lit-card h-full flex flex-col",
        ),
        href=f"/read/{pub['slug']}",
        class_name="block h-full",
    )
