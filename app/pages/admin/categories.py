import reflex as rx
from app.components.admin_layout import admin_layout
from app.states.admin_state import AdminState
from app.states.content_state import ContentState, Category


def _row(cat: Category) -> rx.Component:
    return rx.el.tr(
        rx.el.td(
            rx.el.div(
                rx.icon(cat["emblem"], size=16, class_name="text-[#244a3c]"),
                class_name="w-9 h-9 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec]",
            ),
            class_name="px-4 py-4 align-middle w-14",
        ),
        rx.el.td(
            rx.el.div(
                cat["name"],
                class_name="font-display text-lg text-[#1f2422]",
            ),
            rx.el.div(
                cat["urdu"],
                class_name="font-display text-[#b08b3f] text-lg",
            ),
            class_name="px-4 py-4 align-middle",
        ),
        rx.el.td(
            rx.el.div(
                cat["description"],
                class_name="text-[0.9rem] text-[#3a3f3c] font-serif-body max-w-md",
            ),
            class_name="px-4 py-4 align-middle",
        ),
        rx.el.td(
            rx.el.span(
                f"{cat['count']} pieces",
                class_name="font-mono-caps text-[0.62rem] text-[#6b6558]",
            ),
            class_name="px-4 py-4 align-middle whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.button(
                    rx.icon("pencil", size=14),
                    on_click=AdminState.start_edit_category(cat["slug"]),
                    class_name="p-2 rounded-sm text-[#244a3c] hover:bg-[#efe7d3] transition-colors",
                    title="Edit",
                ),
                rx.el.a(
                    rx.icon("external-link", size=14),
                    href=f"/categories/{cat['slug']}",
                    class_name="p-2 rounded-sm text-[#2c3330] hover:bg-[#efe7d3] transition-colors",
                    title="View section",
                ),
                rx.el.button(
                    rx.icon("trash-2", size=14),
                    on_click=AdminState.delete_category(cat["slug"]),
                    class_name="p-2 rounded-sm text-[#b04a3f] hover:bg-[#f4dcd6] transition-colors",
                    title="Delete",
                ),
                class_name="flex items-center justify-end gap-1",
            ),
            class_name="px-4 py-4 align-middle whitespace-nowrap",
        ),
        class_name="border-b border-[#e4dcc4] hover:bg-[#fbf7ec]/60 transition-colors",
    )


def _form() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.cond(
                    AdminState.cat_editing_slug != "",
                    "Editing category",
                    "New category",
                ),
                class_name="font-mono-caps text-[0.65rem] text-[#b08b3f] mb-3",
            ),
            rx.el.h3(
                rx.cond(
                    AdminState.cat_editing_slug != "",
                    AdminState.cat_form_name,
                    "Add a new room",
                ),
                class_name="font-display text-2xl text-[#1f2422] mb-1",
            ),
            rx.el.p(
                "Sections are the small rooms of the journal. Give one a name, a whisper of Urdu, and a short description.",
                class_name="font-display italic text-[0.9rem] text-[#4a4a44] mb-6",
            ),
            rx.el.div(
                rx.el.label(
                    "Name",
                    class_name="block font-mono-caps text-[0.6rem] text-[#6b6558] mb-2",
                ),
                rx.el.input(
                    type="text",
                    default_value=AdminState.cat_form_name,
                    on_change=AdminState.set_cat_form_name.debounce(250),
                    placeholder="Essays",
                    class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-3 py-2.5 text-[#1f2422] font-serif-body text-[0.95rem] focus:outline-none focus:border-[#244a3c] transition-colors duration-500",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Urdu",
                    class_name="block font-mono-caps text-[0.6rem] text-[#6b6558] mb-2",
                ),
                rx.el.input(
                    type="text",
                    default_value=AdminState.cat_form_urdu,
                    on_change=AdminState.set_cat_form_urdu.debounce(250),
                    placeholder="مضامین",
                    class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-3 py-2.5 text-[#1f2422] font-display text-lg focus:outline-none focus:border-[#244a3c] transition-colors duration-500",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Description",
                    class_name="block font-mono-caps text-[0.6rem] text-[#6b6558] mb-2",
                ),
                rx.el.textarea(
                    default_value=AdminState.cat_form_description,
                    on_change=AdminState.set_cat_form_description.debounce(250),
                    placeholder="A short line about what lives in this section.",
                    rows="3",
                    class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-3 py-2.5 text-[#1f2422] font-serif-body text-[0.95rem] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 resize-y",
                ),
                class_name="mb-4",
            ),
            rx.el.div(
                rx.el.label(
                    "Emblem icon",
                    class_name="block font-mono-caps text-[0.6rem] text-[#6b6558] mb-2",
                ),
                rx.el.div(
                    rx.el.select(
                        rx.foreach(
                            AdminState.emblem_options,
                            lambda o: rx.el.option(o, value=o),
                        ),
                        value=AdminState.cat_form_emblem,
                        on_change=AdminState.set_cat_form_emblem,
                        class_name="appearance-none w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm pl-3 pr-10 py-2.5 font-serif-body text-[0.95rem] text-[#1f2422] focus:outline-none focus:border-[#244a3c] cursor-pointer",
                    ),
                    rx.icon(
                        "chevron-down",
                        size=13,
                        class_name="absolute right-3 top-1/2 -translate-y-1/2 text-[#6b6558] pointer-events-none",
                    ),
                    class_name="relative",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        rx.cond(
                            AdminState.cat_editing_slug != "",
                            "save",
                            "plus",
                        ),
                        size=14,
                    ),
                    rx.el.span(
                        rx.cond(
                            AdminState.cat_editing_slug != "",
                            "Save changes",
                            "Add category",
                        ),
                        class_name="font-mono-caps text-[0.7rem]",
                    ),
                    on_click=AdminState.save_category,
                    class_name="flex-1 inline-flex items-center justify-center gap-2 bg-[#244a3c] text-[#fbf7ec] px-4 py-2.5 rounded-sm hover:bg-[#1f4033] transition-all duration-500",
                ),
                rx.cond(
                    AdminState.cat_editing_slug != "",
                    rx.el.button(
                        rx.icon("x", size=14),
                        on_click=AdminState.start_new_category,
                        class_name="inline-flex items-center gap-2 border border-[#1f2422] text-[#1f2422] px-3 py-2.5 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
                        title="Cancel edit",
                    ),
                    rx.fragment(),
                ),
                class_name="flex items-stretch gap-2",
            ),
            class_name="paper-card rounded-sm p-6",
        ),
        class_name="lg:sticky lg:top-8 h-fit",
    )


def admin_categories_page() -> rx.Component:
    return admin_layout(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    "Sections",
                    class_name="font-mono-caps text-[0.65rem] text-[#b08b3f] mb-3",
                ),
                rx.el.h1(
                    "Categories",
                    class_name="font-display text-4xl md:text-5xl text-[#1f2422]",
                ),
                rx.el.p(
                    "Rooms in the journal. Add, rename, or retire a section — pieces stay attached even when a room is renamed.",
                    class_name="font-display italic text-[#4a4a44] mt-3 max-w-2xl",
                ),
            ),
            class_name="mb-10",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "",
                                    class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                                ),
                                rx.el.th(
                                    "Name",
                                    class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                                ),
                                rx.el.th(
                                    "Description",
                                    class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                                ),
                                rx.el.th(
                                    "Pieces",
                                    class_name="text-left px-4 py-3 font-mono-caps text-[0.6rem] text-[#6b6558] bg-[#efe7d3]/50",
                                ),
                                rx.el.th(
                                    "",
                                    class_name="text-right px-4 py-3 bg-[#efe7d3]/50",
                                ),
                            ),
                        ),
                        rx.el.tbody(
                            rx.foreach(ContentState.categories, _row),
                        ),
                        class_name="table-auto w-full",
                    ),
                    class_name="paper-card rounded-sm overflow-hidden overflow-x-auto",
                ),
                class_name="lg:col-span-2",
            ),
            _form(),
            class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
        ),
        active="categories",
    )
