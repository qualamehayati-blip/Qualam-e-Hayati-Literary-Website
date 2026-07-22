import reflex as rx


def _foot_link(label: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.el.span(label, class_name="link-refined"),
        href=href,
        class_name="text-[0.9rem] text-[#4a4a44] hover:text-[#244a3c] transition-colors duration-500",
    )


def _social(icon: str, href: str) -> rx.Component:
    return rx.el.a(
        rx.icon(icon, size=16, class_name="text-[#4a4a44]"),
        href=href,
        class_name="w-9 h-9 flex items-center justify-center rounded-full border border-[#d9cfb6] hover:border-[#b08b3f] hover:text-[#244a3c] transition-all duration-500",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(class_name="gold-rule opacity-60"),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "feather", size=20, class_name="text-[#244a3c]"
                        ),
                        rx.el.div(
                            "Qualam-e-Hayati",
                            class_name="font-display text-2xl text-[#1f2422]",
                        ),
                        class_name="flex items-center gap-3 mb-4",
                    ),
                    rx.el.p(
                        "A quiet literary journal for essays, fiction, poetry, and correspondence — written, edited, and kept by Mp Kumawat, educator by profession and writer by nature. His work includes Romantic-influenced poetry, original quotations, and daily thoughts, carried from the classrooms of Rajasthan toward an American literary magazine. Printed in light; delivered by evening.",
                        class_name="text-[0.95rem] text-[#4a4a44] leading-relaxed max-w-sm font-serif-body",
                    ),
                    class_name="md:col-span-2",
                ),
                rx.el.div(
                    rx.el.div(
                        "Read",
                        class_name="font-mono-caps text-[0.7rem] text-[#6b6558] mb-4",
                    ),
                    rx.el.div(
                        _foot_link("Home", "/"),
                        _foot_link("Publications", "/publications"),
                        _foot_link("Categories", "/categories"),
                        _foot_link("Bookmarks", "/bookmarks"),
                        class_name="flex flex-col gap-3",
                    ),
                ),
                rx.el.div(
                    rx.el.div(
                        "Journal",
                        class_name="font-mono-caps text-[0.7rem] text-[#6b6558] mb-4",
                    ),
                    rx.el.div(
                        _foot_link("About", "/about"),
                        _foot_link("Contact", "/contact"),
                        _foot_link("Submissions", "/contact"),
                        _foot_link("Feed & Sitemap", "/feed"),
                        class_name="flex flex-col gap-3",
                    ),
                ),
                class_name="grid grid-cols-2 md:grid-cols-4 gap-10 py-14",
            ),
            rx.el.div(class_name="thin-rule"),
            rx.el.div(
                rx.el.div(
                    "© 2025 Qualam-e-Hayati · Written & kept by Mp Kumawat, alone.",
                    class_name="text-[0.85rem] text-[#6b6558] font-serif-body",
                ),
                rx.el.div(
                    _social("mail", "/contact"),
                    _social("book-open", "/publications"),
                    _social("bookmark", "/bookmarks"),
                    _social("rss", "/feed"),
                    _social("feather", "/about"),
                    class_name="flex items-center gap-3",
                ),
                class_name="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 py-8",
            ),
            class_name="max-w-6xl mx-auto px-6 lg:px-10",
        ),
        class_name="bg-[#efe7d3]/50 mt-24",
    )
