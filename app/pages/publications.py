import reflex as rx
from app.components.layout import layout
from app.components.publication_card import publication_card
from app.states.content_state import ContentState


def _page_header() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                "The Archive",
                class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-6 animate-fade-rise",
            ),
            rx.el.h1(
                "Publications",
                class_name="font-display text-6xl md:text-7xl text-[#1f2422] mb-5 animate-fade-rise delay-100",
            ),
            rx.el.div(
                class_name="ornament block text-center animate-fade-rise delay-200"
            ),
            rx.el.p(
                "Every piece we have published, kept together in one quiet room. Read slowly.",
                class_name="font-display italic text-lg md:text-xl text-[#4a4a44] max-w-2xl mx-auto mt-6 animate-fade-rise delay-300",
            ),
            class_name="text-center max-w-3xl mx-auto",
        ),
        class_name="px-6 pt-20 pb-10 md:pt-28",
    )


def _filter_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    size=16,
                    class_name="absolute left-4 top-1/2 -translate-y-1/2 text-[#6b6558]",
                ),
                rx.el.input(
                    type="search",
                    placeholder="Search titles, authors, tags…",
                    default_value=ContentState.search_query,
                    on_change=ContentState.set_search.debounce(300),
                    class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm pl-11 pr-4 py-3 font-serif-body text-[0.98rem] text-[#1f2422] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 placeholder:text-[#a89f8a]",
                ),
                class_name="relative flex-1 min-w-[220px]",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All categories", value="All"),
                    rx.foreach(
                        ContentState.category_names,
                        lambda n: rx.el.option(n, value=n),
                    ),
                    value=ContentState.filter_category,
                    on_change=ContentState.set_filter_category,
                    class_name="appearance-none bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm pl-4 pr-10 py-3 font-serif-body text-[0.95rem] text-[#1f2422] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 cursor-pointer w-full",
                ),
                rx.icon(
                    "chevron-down",
                    size=14,
                    class_name="absolute right-4 top-1/2 -translate-y-1/2 text-[#6b6558] pointer-events-none",
                ),
                class_name="relative min-w-[180px]",
            ),
            rx.el.div(
                rx.el.select(
                    rx.el.option("All years", value="All"),
                    rx.foreach(
                        ContentState.available_years,
                        lambda y: rx.el.option(y, value=y),
                    ),
                    value=ContentState.filter_year,
                    on_change=ContentState.set_filter_year,
                    class_name="appearance-none bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm pl-4 pr-10 py-3 font-serif-body text-[0.95rem] text-[#1f2422] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 cursor-pointer w-full",
                ),
                rx.icon(
                    "chevron-down",
                    size=14,
                    class_name="absolute right-4 top-1/2 -translate-y-1/2 text-[#6b6558] pointer-events-none",
                ),
                class_name="relative min-w-[140px]",
            ),
            rx.cond(
                ContentState.has_active_filters,
                rx.el.button(
                    rx.icon("x", size=14),
                    rx.el.span(
                        "Clear", class_name="font-mono-caps text-[0.7rem]"
                    ),
                    on_click=ContentState.clear_filters,
                    class_name="inline-flex items-center gap-2 border border-[#1f2422] text-[#1f2422] px-4 py-3 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
                ),
                rx.fragment(),
            ),
            class_name="flex flex-col md:flex-row items-stretch md:items-center gap-3 md:gap-4",
        ),
        rx.el.div(
            rx.el.span(
                f"{ContentState.results_count} pieces",
                class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
            ),
            rx.el.span("·", class_name="text-[#b08b3f]"),
            rx.el.span(
                f"Page {ContentState.current_page} of {ContentState.total_pages}",
                class_name="font-mono-caps text-[0.65rem] text-[#6b6558]",
            ),
            class_name="flex items-center gap-3 mt-5",
        ),
        class_name="paper-card rounded-sm p-5 md:p-6",
    )


def _pagination_controls() -> rx.Component:
    return rx.el.div(
        rx.el.button(
            rx.icon("arrow-left", size=14),
            rx.el.span("Previous", class_name="font-mono-caps text-[0.7rem]"),
            on_click=ContentState.go_prev_page,
            disabled=~ContentState.has_prev_page,
            class_name=rx.cond(
                ContentState.has_prev_page,
                "inline-flex items-center gap-2 border border-[#1f2422] text-[#1f2422] px-5 py-3 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
                "inline-flex items-center gap-2 border border-[#d9cfb6] text-[#a89f8a] px-5 py-3 rounded-sm cursor-not-allowed",
            ),
        ),
        rx.el.div(
            rx.el.span(
                f"Page {ContentState.current_page}",
                class_name="font-display text-2xl text-[#1f2422]",
            ),
            rx.el.span(
                "of", class_name="font-mono-caps text-[0.65rem] text-[#6b6558]"
            ),
            rx.el.span(
                ContentState.total_pages,
                class_name="font-display text-2xl text-[#b08b3f]",
            ),
            class_name="flex items-center gap-3",
        ),
        rx.el.button(
            rx.el.span("Next", class_name="font-mono-caps text-[0.7rem]"),
            rx.icon("arrow-right", size=14),
            on_click=ContentState.go_next_page,
            disabled=~ContentState.has_next_page,
            class_name=rx.cond(
                ContentState.has_next_page,
                "inline-flex items-center gap-2 bg-[#244a3c] text-[#fbf7ec] px-5 py-3 rounded-sm hover:bg-[#1f4033] transition-all duration-500",
                "inline-flex items-center gap-2 border border-[#d9cfb6] text-[#a89f8a] px-5 py-3 rounded-sm cursor-not-allowed",
            ),
        ),
        class_name="flex items-center justify-between gap-4 mt-14 pt-10 border-t border-[#e4dcc4]",
    )


def _empty_state() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("search-x", size=32, class_name="text-[#b08b3f]"),
            class_name="w-16 h-16 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec] mb-6 mx-auto",
        ),
        rx.el.h3(
            "No pieces match this search.",
            class_name="font-display text-3xl text-[#1f2422] mb-3",
        ),
        rx.el.p(
            "Try a different word, or clear the filters and wander freely.",
            class_name="font-display italic text-lg text-[#4a4a44] mb-6",
        ),
        rx.el.button(
            "Clear filters",
            on_click=ContentState.clear_filters,
            class_name="font-mono-caps text-[0.72rem] border border-[#1f2422] text-[#1f2422] px-6 py-3 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
        ),
        class_name="paper-card rounded-sm p-14 text-center",
    )


def publications_page() -> rx.Component:
    return layout(
        _page_header(),
        rx.el.section(
            rx.el.div(
                _filter_bar(),
                class_name="max-w-6xl mx-auto px-6 lg:px-10 mb-10",
            ),
            class_name="",
        ),
        rx.el.section(
            rx.el.div(
                rx.cond(
                    ContentState.results_count > 0,
                    rx.el.div(
                        rx.el.div(
                            rx.foreach(
                                ContentState.paginated_publications,
                                lambda p: publication_card(p),
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 md:gap-8",
                        ),
                        _pagination_controls(),
                    ),
                    _empty_state(),
                ),
                class_name="max-w-6xl mx-auto px-6 lg:px-10",
            ),
            class_name="pb-24",
        ),
    )
