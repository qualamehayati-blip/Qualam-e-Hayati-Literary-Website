import reflex as rx
from app.components.admin_layout import admin_layout
from app.states.admin_state import AdminState
from app.states.content_state import Publication


def _stat_card(
    label: str, value: str | int | rx.Var, icon: str, tint: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                icon,
                size=18,
                class_name=rx.cond(
                    tint == "[#244a3c]",
                    "text-[#244a3c]",
                    "text-[#b08b3f]",
                ),
            ),
            class_name="w-11 h-11 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec] mb-4",
        ),
        rx.el.div(
            value,
            class_name="font-display text-4xl text-[#1f2422] leading-none",
        ),
        rx.el.div(
            label,
            class_name="font-mono-caps text-[0.62rem] text-[#6b6558] mt-2",
        ),
        class_name="paper-card rounded-sm p-6",
    )


def _status_pill(status) -> rx.Component:
    return rx.cond(
        status == "published",
        rx.el.span(
            rx.icon("circle-check", size=11),
            rx.el.span("Published", class_name="font-mono-caps text-[0.58rem]"),
            class_name="inline-flex items-center gap-1.5 px-2 py-1 rounded-full bg-[#e2ecd6] text-[#244a3c] border border-[#c9d8b8]",
        ),
        rx.el.span(
            rx.icon("pencil", size=11),
            rx.el.span("Draft", class_name="font-mono-caps text-[0.58rem]"),
            class_name="inline-flex items-center gap-1.5 px-2 py-1 rounded-full bg-[#f4ebd6] text-[#8a6a1f] border border-[#e2d3a8]",
        ),
    )


def _pub_row(pub: Publication) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    pub["title"],
                    class_name="font-display text-lg text-[#1f2422] leading-tight",
                ),
                rx.el.div(
                    pub["subtitle"],
                    class_name="font-display italic text-[0.9rem] text-[#6b6558] mt-0.5",
                ),
                class_name="min-w-0",
            ),
            class_name="px-4 py-4 align-top",
        ),
        rx.el.td(
            rx.el.span(
                pub["category"],
                class_name="font-mono-caps text-[0.62rem] text-[#b08b3f]",
            ),
            class_name="px-4 py-4 align-top whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(
                pub["author"],
                class_name="text-[0.9rem] text-[#2c3330]",
            ),
            class_name="px-4 py-4 align-top whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(
                pub["date"],
                class_name="font-mono-caps text-[0.6rem] text-[#6b6558]",
            ),
            class_name="px-4 py-4 align-top whitespace-nowrap",
        ),
        rx.el.td(
            _status_pill(pub["status"]),
            class_name="px-4 py-4 align-top whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.a(
                    rx.icon("eye", size=14),
                    href=f"/read/{pub['slug']}",
                    class_name="p-2 rounded-sm text-[#2c3330] hover:bg-[#efe7d3] transition-colors",
                    title="Preview",
                ),
                rx.el.a(
                    rx.icon("pencil", size=14),
                    href=f"/admin/publications/edit/{pub['slug']}",
                    class_name="p-2 rounded-sm text-[#244a3c] hover:bg-[#efe7d3] transition-colors",
                    title="Edit",
                ),
                rx.el.button(
                    rx.cond(
                        pub["status"] == "published",
                        rx.icon("archive", size=14),
                        rx.icon("send", size=14),
                    ),
                    on_click=AdminState.toggle_publish(pub["slug"]),
                    class_name="p-2 rounded-sm text-[#b08b3f] hover:bg-[#efe7d3] transition-colors",
                    title="Toggle publish state",
                ),
                rx.el.button(
                    rx.icon("trash-2", size=14),
                    on_click=AdminState.delete_publication(pub["slug"]),
                    class_name="p-2 rounded-sm text-[#b04a3f] hover:bg-[#f4dcd6] transition-colors",
                    title="Delete",
                ),
                class_name="flex items-center gap-1 justify-end",
            ),
            class_name="px-4 py-4 align-top whitespace-nowrap",
        ),
        class_name="border-b border-[#e4dcc4] hover:bg-[#fbf7ec]/60 transition-colors",
    )


def _filter_pill(label: str, value: str) -> rx.Component:
    return rx.el.button(
        label,
        on_click=AdminState.set_dashboard_filter(value),
        class_name=rx.cond(
            AdminState.dashboard_filter == value,
            "font-mono-caps text-[0.62rem] px-3 py-1.5 rounded-full bg-[#244a3c] text-[#fbf7ec] transition-all duration-300",
            "font-mono-caps text-[0.62rem] px-3 py-1.5 rounded-full border border-[#d9cfb6] text-[#2c3330] hover:border-[#b08b3f] transition-all duration-300",
        ),
    )


def _table() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                _filter_pill("All", "all"),
                _filter_pill("Published", "published"),
                _filter_pill("Drafts", "draft"),
                class_name="flex items-center gap-2 flex-wrap",
            ),
            rx.el.div(
                rx.icon(
                    "search",
                    size=14,
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 text-[#6b6558]",
                ),
                rx.el.input(
                    type="search",
                    placeholder="Search title, author, category…",
                    default_value=AdminState.dashboard_search,
                    on_change=AdminState.set_dashboard_search.debounce(250),
                    class_name="bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm pl-9 pr-3 py-2 font-serif-body text-[0.9rem] text-[#1f2422] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 w-full sm:w-72",
                ),
                class_name="relative",
            ),
            class_name="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mb-5",
        ),
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Title",
                            class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                        ),
                        rx.el.th(
                            "Category",
                            class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                        ),
                        rx.el.th(
                            "Author",
                            class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                        ),
                        rx.el.th(
                            "Date",
                            class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                        ),
                        rx.el.th(
                            "",
                            class_name="text-right px-4 py-3 bg-[#efe7d3]/50",
                        ),
                    ),
                ),
                rx.el.tbody(
                    rx.foreach(AdminState.dashboard_publications, _pub_row),
                ),
                class_name="table-auto w-full",
            ),
            class_name="paper-card rounded-sm overflow-hidden overflow-x-auto",
        ),
        rx.cond(
            AdminState.dashboard_publications.length() == 0,
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "book-open",
                        size=22,
                        class_name="text-[#b08b3f] mx-auto mb-3",
                    ),
                    rx.el.p(
                        "No pieces match this view.",
                        class_name="font-display italic text-[#4a4a44]",
                    ),
                    class_name="text-center py-10",
                ),
                class_name="",
            ),
            rx.fragment(),
        ),
    )


def _step(number: str, title: str, body: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                number,
                class_name="font-display text-2xl text-[#b08b3f] leading-none",
            ),
            rx.icon(icon, size=16, class_name="text-[#244a3c]"),
            class_name="flex items-center justify-between mb-3",
        ),
        rx.el.div(
            title,
            class_name="font-display text-lg text-[#1f2422] mb-1",
        ),
        rx.el.p(
            body,
            class_name="font-serif-body text-[0.88rem] text-[#4a4a44] leading-relaxed",
        ),
        class_name="paper-card rounded-sm p-5 h-full",
    )


def _onboarding() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    "Welcome, Mp Kumawat",
                    class_name="font-mono-caps text-[0.62rem] text-[#b08b3f] mb-2",
                ),
                rx.el.h2(
                    "How to publish your own writing",
                    class_name="font-display text-2xl md:text-3xl text-[#1f2422] mb-2",
                ),
                rx.el.p(
                    "This journal belongs to you \u2014 you are the only author and the only editor. Four small steps to move a piece from lamp to page.",
                    class_name="font-display italic text-[0.98rem] text-[#4a4a44] max-w-2xl",
                ),
            ),
            rx.el.a(
                rx.icon("plus", size=14),
                rx.el.span(
                    "Begin a new piece",
                    class_name="font-mono-caps text-[0.68rem]",
                ),
                href="/admin/publications/new",
                class_name="hidden md:inline-flex items-center gap-2 bg-[#244a3c] text-[#fbf7ec] px-4 py-2.5 rounded-sm hover:bg-[#1f4033] transition-all duration-500 shrink-0",
            ),
            class_name="flex flex-col md:flex-row md:items-start md:justify-between gap-4 mb-6",
        ),
        rx.el.div(
            _step(
                "1.",
                "Sign in",
                "You are already at the editorial desk. Only you can reach these rooms \u2014 there is no public sign-up.",
                "lock-keyhole",
            ),
            _step(
                "2.",
                "Write in Markdown",
                "Open \u2018New piece\u2019, give it a title and a category, and write the body in plain Markdown \u2014 headings, lists, quotes, images.",
                "pen-line",
            ),
            _step(
                "3.",
                "Save draft or publish",
                "Save a draft to keep it on your desk, or publish now to send it into the journal. You can move it between the two at any time.",
                "send",
            ),
            _step(
                "4.",
                "It appears publicly",
                "Published pieces show up immediately on the home page, the archive, the section rooms, and the feed \u2014 signed under your name.",
                "book-open",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4",
        ),
        rx.cond(
            AdminState.has_starter_content,
            rx.el.div(
                rx.el.div(class_name="thin-rule my-6"),
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "info",
                                size=14,
                                class_name="text-[#b08b3f]",
                            ),
                            rx.el.span(
                                "Starter content",
                                class_name="font-mono-caps text-[0.6rem] text-[#b08b3f]",
                            ),
                            class_name="inline-flex items-center gap-2 mb-2",
                        ),
                        rx.el.div(
                            f"{AdminState.starter_count} sample pieces are currently on display",
                            class_name="font-display text-lg text-[#1f2422] mb-1",
                        ),
                        rx.el.p(
                            "These are placeholder writings kept in the journal so first-time visitors see a full room. They are not by you. Clear them when your own writing is ready to stand alone \u2014 or leave them for now; either is fine.",
                            class_name="font-serif-body text-[0.9rem] text-[#4a4a44] leading-relaxed max-w-2xl",
                        ),
                        class_name="flex-1",
                    ),
                    rx.el.button(
                        rx.icon("trash-2", size=13),
                        rx.el.span(
                            "Clear starter content",
                            class_name="font-mono-caps text-[0.65rem]",
                        ),
                        on_click=AdminState.clear_starter_content,
                        class_name="inline-flex items-center gap-2 border border-[#1f2422] text-[#1f2422] px-4 py-2.5 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500 shrink-0 h-fit",
                    ),
                    class_name="flex flex-col md:flex-row md:items-center md:justify-between gap-4",
                ),
            ),
            rx.fragment(),
        ),
        class_name="paper-card rounded-sm p-6 md:p-8 mb-10",
    )


def admin_dashboard_page() -> rx.Component:
    return admin_layout(
        _onboarding(),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    "Editorial Desk",
                    class_name="font-mono-caps text-[0.65rem] text-[#b08b3f] mb-3",
                ),
                rx.el.h1(
                    "Your Writing",
                    class_name="font-display text-4xl md:text-5xl text-[#1f2422]",
                ),
                rx.el.p(
                    "Every piece in the journal, in one quiet room. Publish, unpublish, revise, or set something aside as a draft.",
                    class_name="font-display italic text-[#4a4a44] mt-3 max-w-2xl",
                ),
            ),
            rx.el.a(
                rx.icon("plus", size=14),
                rx.el.span(
                    "New piece", class_name="font-mono-caps text-[0.7rem]"
                ),
                href="/admin/publications/new",
                class_name="inline-flex items-center gap-2 bg-[#244a3c] text-[#fbf7ec] px-5 py-3 rounded-sm hover:bg-[#1f4033] transition-all duration-500",
            ),
            class_name="flex flex-col md:flex-row md:items-end md:justify-between gap-5 mb-10",
        ),
        rx.el.div(
            _stat_card(
                "All pieces",
                AdminState.total_publications,
                "book",
                "[#244a3c]",
            ),
            _stat_card(
                "Published",
                AdminState.total_published,
                "circle-check",
                "[#244a3c]",
            ),
            _stat_card(
                "Drafts",
                AdminState.total_drafts,
                "pencil",
                "[#b08b3f]",
            ),
            _stat_card(
                "Categories",
                AdminState.total_categories,
                "folder",
                "[#b08b3f]",
            ),
            class_name="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-5 mb-10",
        ),
        _table(),
        active="dashboard",
    )
