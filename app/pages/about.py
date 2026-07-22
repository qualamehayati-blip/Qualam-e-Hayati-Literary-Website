import reflex as rx
from app.components.layout import layout


def _principle(number: str, title: str, body: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            number, class_name="font-display text-5xl text-[#b08b3f] mb-4"
        ),
        rx.el.h3(title, class_name="font-display text-2xl text-[#1f2422] mb-3"),
        rx.el.p(
            body,
            class_name="text-[0.98rem] text-[#3a3f3c] leading-relaxed font-serif-body",
        ),
        class_name="paper-card rounded-sm p-8 lit-card h-full",
    )


def _editor(name: str, role: str, note: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.img(
                src="/placeholder.svg",
                alt="Portrait of Mp Kumawat, educator, writer, and editor of Qualam-e-Hayati",
                width="100%",
                height="100%",
                loading="lazy",
                decoding="async",
                class_name="w-full h-full object-cover",
            ),
            class_name="w-36 h-36 md:w-44 md:h-44 shrink-0 rounded-full overflow-hidden border border-[#d9cfb6] bg-[#fbf7ec]",
        ),
        rx.el.div(
            rx.el.div(
                name, class_name="font-display text-2xl text-[#1f2422] mb-1"
            ),
            rx.el.div(
                role,
                class_name="font-mono-caps text-[0.65rem] text-[#b08b3f] mb-4",
            ),
            rx.el.p(
                "Hello, and welcome. I am an educator by profession and a writer by nature. As a literature educator and Head of Department, I carry the attentiveness of the classroom into my creative work — Romantic-influenced poetry, original quotations, daily thoughts, and the quiet conversation between a reader and a sentence.",
                class_name="text-[0.98rem] text-[#3a3f3c] leading-relaxed font-serif-body mb-4",
            ),
            rx.el.p(
                note,
                class_name="text-[0.95rem] text-[#3a3f3c] leading-relaxed font-serif-body italic",
            ),
            class_name="flex-1",
        ),
        rx.el.div(
            rx.el.div(class_name="ornament block mb-4"),
            rx.el.blockquote(
                rx.el.p(
                    "Poetry is the spontaneous overflow of powerful feelings.",
                    class_name="font-display italic text-2xl md:text-3xl text-[#1f2422] leading-relaxed",
                ),
                rx.el.footer(
                    "— William Wordsworth · a sentence I keep close to the work",
                    class_name="font-mono-caps text-[0.65rem] text-[#6b6558] mt-4",
                ),
                class_name="text-left",
            ),
            class_name="border-t border-[#e4dcc4] pt-6 mt-7",
        ),
        class_name="paper-card rounded-sm p-7 md:p-8 lit-card h-full",
    )


def about_page() -> rx.Component:
    return layout(
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    "About",
                    class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-6 animate-fade-rise",
                ),
                rx.el.h1(
                    "A quiet journal, kept carefully.",
                    class_name="font-display text-5xl md:text-6xl lg:text-7xl leading-[1.05] text-[#1f2422] mb-8 animate-fade-rise delay-100",
                ),
                rx.el.div(
                    class_name="ornament block animate-fade-rise delay-200"
                ),
                rx.el.p(
                    "Qualam-e-Hayati — قلمِ حیاتی, the pen of a lived life — is a digital literary journal for essays, fiction, poetry, interviews, and correspondence. It is the literary home of Mp Kumawat: an educator by profession, a writer by nature, a literature educator and Head of Department whose creative portfolio moves between Romantic-influenced poetry, original quotations, and daily thoughts. His journey begins in the classrooms of Rajasthan and reaches toward the pages of an American literary magazine — carrying the quiet conviction that a life in education and a life in literature can illuminate one another.",
                    class_name="font-display italic text-xl md:text-2xl text-[#3a3f3c] leading-relaxed max-w-3xl mt-8 animate-fade-rise delay-300",
                ),
                class_name="max-w-5xl mx-auto",
            ),
            class_name="px-6 lg:px-10 pt-20 pb-16 md:pt-28",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "Our Ledger",
                        class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-3",
                    ),
                    rx.el.h2(
                        "Three quiet principles of the journal",
                        class_name="font-display text-4xl md:text-5xl text-[#1f2422]",
                    ),
                    class_name="mb-12",
                ),
                rx.el.div(
                    _principle(
                        "I.",
                        "Slowness on purpose",
                        "We publish less, so that each piece may earn its place at the table. A single essay, well tended, is worth a season of hurry.",
                    ),
                    _principle(
                        "II.",
                        "The reader is a guest",
                        "We do not write to be admired; we write to be honest. Understanding, when it comes, arrives from a stranger at an odd hour.",
                    ),
                    _principle(
                        "III.",
                        "The lamp before the lens",
                        "We favor the small, warm, particular light — kitchens, verandas, buses, evenings — over any promise of the panoramic.",
                    ),
                    class_name="grid grid-cols-1 md:grid-cols-3 gap-6 md:gap-8",
                ),
                class_name="max-w-5xl mx-auto px-6 lg:px-10",
            ),
            class_name="py-16",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        "About the Author",
                        class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-3",
                    ),
                    rx.el.h2(
                        "A single hand, a single lamp",
                        class_name="font-display text-4xl md:text-5xl text-[#1f2422]",
                    ),
                    rx.el.p(
                        "There is no staff here — no committee, no rotating masthead. Qualam-e-Hayati is written, edited, designed, and kept in order by Mp Kumawat, an educator by profession and writer by nature. As a literature educator and Head of Department, he carries the attentiveness of the classroom into his creative work: Romantic-influenced poetry, original quotations, daily thoughts, and the long conversation between a reader and a sentence.",
                        class_name="font-display italic text-lg text-[#4a4a44] mt-4 max-w-2xl",
                    ),
                    class_name="mb-12",
                ),
                rx.el.div(
                    _editor(
                        "Mp Kumawat",
                        "Educator · Head of Department · Writer · Editor",
                        "I trust sentences the way I trust doorframes — the load-bearing kind, quietly made. I came to literature through the classrooms of Rajasthan, where teaching made me attentive to the lives held inside words. Today, as a literature educator, Head of Department, and writer, I keep making room for Romantic-influenced poems, original quotations, and daily thoughts — work that has travelled from those classrooms toward an American literary magazine, while remaining rooted in the ordinary human voice.",
                    ),
                    class_name="max-w-4xl mx-auto",
                ),
                class_name="max-w-5xl mx-auto px-6 lg:px-10",
            ),
            class_name="py-20",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Write to us.",
                        class_name="font-display text-4xl md:text-5xl text-[#1f2422] mb-4",
                    ),
                    rx.el.p(
                        "Whether you have a piece to submit, a correction to send, or simply a small remark to leave in the margin — the door is open.",
                        class_name="font-display italic text-lg text-[#4a4a44] max-w-xl mx-auto mb-8",
                    ),
                    rx.el.a(
                        rx.el.span(
                            "Open the letterbox",
                            class_name="font-mono-caps text-[0.72rem]",
                        ),
                        rx.icon("arrow-right", size=14),
                        href="/contact",
                        class_name="inline-flex items-center gap-3 bg-[#244a3c] text-[#fbf7ec] px-8 py-4 rounded-sm hover:bg-[#1f4033] transition-all duration-500 hover:gap-4",
                    ),
                    class_name="text-center max-w-2xl mx-auto",
                ),
                class_name="max-w-5xl mx-auto px-6 lg:px-10",
            ),
            class_name="py-20",
        ),
    )
