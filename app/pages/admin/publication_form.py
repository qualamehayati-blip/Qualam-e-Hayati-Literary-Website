import reflex as rx
from app.components.admin_layout import admin_layout
from app.states.admin_state import AdminState
from app.states.content_state import ContentState


_MARKDOWN_STARTER = """## A section heading

Open with a short paragraph — the way one begins a letter, without hurry.

- A list item
- A second thought
- A third

> A blockquote, for a line worth pausing on.

Here is `some inline code`, and below, a code block:

```python
def hello():
    print("Hello, reader.")
```

![Alt text for an image](https://example.com/image.jpg)
"""


def _label(text: str) -> rx.Component:
    return rx.el.label(
        text,
        class_name="block font-mono-caps text-[0.62rem] text-[#6b6558] mb-2",
    )


def _text_field(
    label: str,
    key: str,
    value,
    on_change,
    placeholder: str = "",
    input_type: str = "text",
) -> rx.Component:
    return rx.el.div(
        _label(label),
        rx.el.input(
            type=input_type,
            default_value=value,
            on_change=on_change.debounce(250),
            placeholder=placeholder,
            class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-4 py-3 text-[#1f2422] font-serif-body text-[0.98rem] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 placeholder:text-[#a89f8a]",
        ),
        class_name="mb-5",
    )


def _textarea_field(
    label: str,
    key: str,
    value,
    on_change,
    placeholder: str = "",
    rows: str = "5",
) -> rx.Component:
    return rx.el.div(
        _label(label),
        rx.el.textarea(
            default_value=value,
            on_change=on_change.debounce(250),
            placeholder=placeholder,
            rows=rows,
            class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-4 py-3 text-[#1f2422] font-serif-body text-[0.98rem] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 placeholder:text-[#a89f8a] resize-y",
        ),
        class_name="mb-5",
    )


def _select_field(label: str, value, options, on_change) -> rx.Component:
    return rx.el.div(
        _label(label),
        rx.el.div(
            rx.el.select(
                rx.foreach(options, lambda o: rx.el.option(o, value=o)),
                value=value,
                on_change=on_change,
                class_name="appearance-none w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm pl-4 pr-10 py-3 font-serif-body text-[0.95rem] text-[#1f2422] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 cursor-pointer",
            ),
            rx.icon(
                "chevron-down",
                size=14,
                class_name="absolute right-4 top-1/2 -translate-y-1/2 text-[#6b6558] pointer-events-none",
            ),
            class_name="relative",
        ),
        class_name="mb-5",
    )


def _md_toolbar_button(label: str, icon: str, snippet: str) -> rx.Component:
    return rx.el.button(
        rx.icon(icon, size=13),
        rx.el.span(label, class_name="font-mono-caps text-[0.6rem]"),
        on_click=AdminState.insert_snippet(snippet),
        type="button",
        class_name="inline-flex items-center gap-1.5 px-2.5 py-1.5 rounded-sm border border-[#d9cfb6] text-[#2c3330] hover:border-[#b08b3f] hover:text-[#244a3c] transition-all duration-300",
        title=label,
    )


def _markdown_editor() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            _label("Body — Markdown"),
            rx.el.button(
                rx.cond(
                    AdminState.preview_mode,
                    rx.fragment(
                        rx.icon("pencil", size=13),
                        rx.el.span(
                            "Edit", class_name="font-mono-caps text-[0.62rem]"
                        ),
                    ),
                    rx.fragment(
                        rx.icon("eye", size=13),
                        rx.el.span(
                            "Preview",
                            class_name="font-mono-caps text-[0.62rem]",
                        ),
                    ),
                ),
                on_click=AdminState.toggle_preview,
                type="button",
                class_name="inline-flex items-center gap-1.5 border border-[#1f2422] text-[#1f2422] px-3 py-1.5 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
            ),
            class_name="flex items-center justify-between mb-2",
        ),
        rx.cond(
            AdminState.preview_mode,
            rx.el.div(
                rx.markdown(
                    AdminState.form_body_markdown,
                    class_name="prose-lit admin-markdown",
                ),
                class_name="paper-card rounded-sm p-6 min-h-[420px]",
            ),
            rx.el.div(
                rx.el.div(
                    _md_toolbar_button("H2", "heading-2", "## Section heading"),
                    _md_toolbar_button("H3", "heading-3", "### Subheading"),
                    _md_toolbar_button("Bold", "bold", "**bold text**"),
                    _md_toolbar_button("Italic", "italic", "*italic text*"),
                    _md_toolbar_button(
                        "List",
                        "list",
                        "- first item\n- second item\n- third item",
                    ),
                    _md_toolbar_button(
                        "Numbered",
                        "list-ordered",
                        "1. first\n2. second\n3. third",
                    ),
                    _md_toolbar_button(
                        "Quote", "quote", "> A line worth pausing on."
                    ),
                    _md_toolbar_button(
                        "Link", "link", "[link text](https://example.com)"
                    ),
                    _md_toolbar_button(
                        "Image",
                        "image",
                        "![alt text](https://example.com/image.jpg)",
                    ),
                    _md_toolbar_button(
                        "Code",
                        "code",
                        "```python\n# code here\n```",
                    ),
                    _md_toolbar_button("Divider", "minus", "\n---\n"),
                    class_name="flex flex-wrap items-center gap-1.5 mb-2 p-2 bg-[#efe7d3]/40 border border-[#d9cfb6] rounded-sm",
                ),
                rx.el.textarea(
                    default_value=AdminState.form_body_markdown,
                    on_change=AdminState.set_form_body_markdown.debounce(250),
                    placeholder=_MARKDOWN_STARTER,
                    rows="22",
                    class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-4 py-3 text-[#1f2422] font-mono text-[0.9rem] leading-relaxed focus:outline-none focus:border-[#244a3c] transition-colors duration-500 placeholder:text-[#a89f8a] resize-y",
                ),
                rx.el.p(
                    "Supports Markdown: # heading, - list, > blockquote, `code`, ```code blocks```, ![images](url), and [links](url).",
                    class_name="mt-2 font-display italic text-[0.82rem] text-[#6b6558]",
                ),
            ),
        ),
        class_name="",
    )


def _sidebar_panel() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                "Status",
                class_name="font-mono-caps text-[0.65rem] text-[#b08b3f] mb-3",
            ),
            rx.cond(
                AdminState.form_status == "published",
                rx.el.div(
                    rx.icon(
                        "circle-check", size=13, class_name="text-[#244a3c]"
                    ),
                    rx.el.span(
                        "Live in the journal",
                        class_name="font-mono-caps text-[0.65rem] text-[#244a3c]",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-[#e2ecd6] border border-[#c9d8b8]",
                ),
                rx.el.div(
                    rx.icon("pencil", size=13, class_name="text-[#8a6a1f]"),
                    rx.el.span(
                        "Draft — not visible to readers",
                        class_name="font-mono-caps text-[0.65rem] text-[#8a6a1f]",
                    ),
                    class_name="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-[#f4ebd6] border border-[#e2d3a8]",
                ),
            ),
            class_name="mb-6",
        ),
        rx.el.div(class_name="thin-rule mb-6"),
        rx.el.div(
            rx.el.button(
                rx.icon("save", size=14),
                rx.el.span(
                    "Save draft", class_name="font-mono-caps text-[0.7rem]"
                ),
                on_click=AdminState.save_draft,
                type="button",
                class_name="w-full inline-flex items-center justify-center gap-2 border border-[#1f2422] text-[#1f2422] px-4 py-3 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500 mb-3",
            ),
            rx.el.button(
                rx.icon("send", size=14),
                rx.el.span(
                    "Publish now", class_name="font-mono-caps text-[0.7rem]"
                ),
                on_click=AdminState.publish_now,
                type="button",
                class_name="w-full inline-flex items-center justify-center gap-2 bg-[#244a3c] text-[#fbf7ec] px-4 py-3 rounded-sm hover:bg-[#1f4033] transition-all duration-500",
            ),
            class_name="mb-6",
        ),
        rx.cond(
            AdminState.editing_slug != "",
            rx.el.div(
                rx.el.div(class_name="thin-rule mb-6"),
                rx.el.a(
                    rx.icon("eye", size=13),
                    rx.el.span(
                        "Preview on site",
                        class_name="font-mono-caps text-[0.65rem]",
                    ),
                    href=f"/read/{AdminState.editing_slug}",
                    target="_blank",
                    class_name="inline-flex items-center gap-2 text-[#244a3c] hover:text-[#1f4033] transition-colors",
                ),
                class_name="",
            ),
            rx.fragment(),
        ),
        class_name="paper-card rounded-sm p-6 h-fit lg:sticky lg:top-8",
    )


def publication_form_page() -> rx.Component:
    return admin_layout(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", size=13),
                rx.el.span(
                    "Back to dashboard",
                    class_name="font-mono-caps text-[0.65rem] link-refined",
                ),
                href="/admin",
                class_name="inline-flex items-center gap-2 text-[#244a3c] mb-6",
            ),
            rx.el.div(
                rx.cond(
                    AdminState.editing_slug != "",
                    "Revise a piece",
                    "Write a new piece",
                ),
                class_name="font-mono-caps text-[0.65rem] text-[#b08b3f] mb-3",
            ),
            rx.el.h1(
                rx.cond(
                    AdminState.editing_slug != "",
                    AdminState.form_title,
                    "Untitled",
                ),
                class_name="font-display text-4xl md:text-5xl text-[#1f2422] mb-2 leading-tight",
            ),
            rx.el.p(
                rx.cond(
                    AdminState.form_subtitle != "",
                    AdminState.form_subtitle,
                    "Every piece is edited the way one might trim a lamp.",
                ),
                class_name="font-display italic text-[#4a4a44] mb-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        _text_field(
                            "Title",
                            AdminState.editing_slug + "-title",
                            AdminState.form_title,
                            AdminState.set_form_title,
                            "The title of the piece",
                        ),
                        _text_field(
                            "Subtitle",
                            AdminState.editing_slug + "-subtitle",
                            AdminState.form_subtitle,
                            AdminState.set_form_subtitle,
                            "A short subtitle or dedication",
                        ),
                        rx.el.div(
                            _text_field(
                                "Author",
                                AdminState.editing_slug + "-author",
                                AdminState.form_author,
                                AdminState.set_form_author,
                                "Mp Kumawat",
                            ),
                            _select_field(
                                "Category",
                                AdminState.form_category,
                                ContentState.category_names,
                                AdminState.set_form_category,
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                        ),
                        rx.el.div(
                            _text_field(
                                "Date",
                                AdminState.editing_slug + "-date",
                                AdminState.form_date,
                                AdminState.set_form_date,
                                "March 14, 2025",
                            ),
                            _text_field(
                                "Year",
                                AdminState.editing_slug + "-year",
                                AdminState.form_year,
                                AdminState.set_form_year,
                                "2025",
                            ),
                            _text_field(
                                "Read time (min)",
                                AdminState.editing_slug + "-read",
                                AdminState.form_read_minutes.to_string(),
                                AdminState.set_form_read_minutes,
                                "5",
                                input_type="number",
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-3 gap-4",
                        ),
                        _textarea_field(
                            "Excerpt",
                            AdminState.editing_slug + "-excerpt",
                            AdminState.form_excerpt,
                            AdminState.set_form_excerpt,
                            "A short teaser — a sentence or two.",
                            rows="3",
                        ),
                        _text_field(
                            "Tags (comma-separated)",
                            AdminState.editing_slug + "-tags",
                            AdminState.form_tags,
                            AdminState.set_form_tags,
                            "memory, language, hope",
                        ),
                        rx.el.div(
                            _select_field(
                                "Cover emblem",
                                AdminState.form_cover_emblem,
                                AdminState.emblem_options,
                                AdminState.set_form_cover_emblem,
                            ),
                            _text_field(
                                "Cover image URL (optional)",
                                AdminState.editing_slug + "-cover-img",
                                AdminState.form_cover_image,
                                AdminState.set_form_cover_image,
                                "https://…/image.jpg",
                            ),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
                        ),
                        rx.cond(
                            AdminState.form_cover_image != "",
                            rx.el.div(
                                rx.el.div(
                                    "Cover preview",
                                    class_name="font-mono-caps text-[0.6rem] text-[#6b6558] mb-2",
                                ),
                                rx.el.img(
                                    src=AdminState.form_cover_image,
                                    alt="Cover preview",
                                    loading="lazy",
                                    decoding="async",
                                    class_name="w-full max-h-64 object-cover rounded-sm border border-[#d9cfb6]",
                                ),
                                class_name="mb-6",
                            ),
                            rx.fragment(),
                        ),
                        rx.el.div(class_name="thin-rule my-8"),
                        _markdown_editor(),
                        class_name="paper-card rounded-sm p-6 md:p-8",
                    ),
                    class_name="lg:col-span-2",
                ),
                _sidebar_panel(),
                class_name="grid grid-cols-1 lg:grid-cols-3 gap-6",
            ),
            class_name="",
        ),
        active="new",
    )
