import reflex as rx

from app.runtime_compat import install_runtime_compatibility_patch

install_runtime_compatibility_patch()

from app.pages.home import home_page
from app.pages.publications import publications_page
from app.pages.categories import categories_page, category_detail_page
from app.pages.reading import reading_page
from app.pages.about import about_page
from app.pages.contact import contact_page
from app.pages.bookmarks import bookmarks_page
from app.pages.feed import feed_page
from app.pages.admin.login import admin_login_page
from app.pages.admin.dashboard import admin_dashboard_page
from app.pages.admin.publication_form import publication_form_page
from app.pages.admin.categories import admin_categories_page
from app.states.auth_state import AuthState
from app.states.admin_state import AdminState


def index() -> rx.Component:
    return home_page()


app = rx.App(
    stylesheets=["/theme.css"],
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect",
            href="https://fonts.gstatic.com",
            cross_origin="",
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Lora:ital,wght@0,400;0,500;0,600;1,400;1,500&display=swap",
            rel="stylesheet",
        ),
    ],
    theme=rx.theme(appearance="light"),
)

# SEO metadata shared across pages
_SITE_KEYWORDS = "literary journal, essays, fiction, poetry, urdu literature, qalam-e-hayati, qualam-e-hayati"

# ---------------------------------------------------------------
# Admin routes — dynamic edit route registered before static ones.
# Every admin page is gated by AuthState.require_auth on_load.
# ---------------------------------------------------------------
app.add_page(
    publication_form_page,
    route="/admin/publications/edit/[slug]",
    title="Edit piece — Editorial Desk",
    description="Editorial desk (private).",
    meta=[{"name": "robots", "content": "noindex, nofollow"}],
    on_load=AdminState.load_edit_form,
)
app.add_page(
    publication_form_page,
    route="/admin/publications/new",
    title="New piece — Editorial Desk",
    description="Editorial desk (private).",
    meta=[{"name": "robots", "content": "noindex, nofollow"}],
    on_load=AdminState.load_new_form,
)
app.add_page(
    admin_categories_page,
    route="/admin/categories",
    title="Categories — Editorial Desk",
    description="Editorial desk (private).",
    meta=[{"name": "robots", "content": "noindex, nofollow"}],
    on_load=AuthState.require_auth,
)
app.add_page(
    admin_login_page,
    route="/admin/login",
    title="Sign in — Editorial Desk",
    description="Private editors' door.",
    meta=[{"name": "robots", "content": "noindex, nofollow"}],
    on_load=AuthState.redirect_if_authenticated,
)
app.add_page(
    admin_dashboard_page,
    route="/admin",
    title="Editorial Desk — Qualam-e-Hayati",
    description="Private editors' desk.",
    meta=[{"name": "robots", "content": "noindex, nofollow"}],
    on_load=AuthState.require_auth,
)

# Dynamic routes registered before static index.
app.add_page(
    reading_page,
    route="/read/[slug]",
    title="Reading — Qualam-e-Hayati",
    description="Read a piece from Qualam-e-Hayati, a literary journal for essays, fiction, poetry, and correspondence.",
    meta=[
        {"name": "keywords", "content": _SITE_KEYWORDS},
        {"property": "og:type", "content": "article"},
        {"property": "og:site_name", "content": "Qualam-e-Hayati"},
    ],
)
app.add_page(
    category_detail_page,
    route="/categories/[slug]",
    title="Category — Qualam-e-Hayati",
    description="Browse a category of writing in Qualam-e-Hayati — essays, fiction, poetry, interviews, or letters.",
    meta=[{"name": "keywords", "content": _SITE_KEYWORDS}],
)
app.add_page(
    categories_page,
    route="/categories",
    title="Categories — Qualam-e-Hayati",
    description="Five rooms in a small house — essays, fiction, poetry, interviews, letters.",
    meta=[{"name": "keywords", "content": _SITE_KEYWORDS}],
)
app.add_page(
    publications_page,
    route="/publications",
    title="Publications — Qualam-e-Hayati",
    description="The complete archive of Qualam-e-Hayati. Search, filter, and browse every published piece.",
    meta=[{"name": "keywords", "content": _SITE_KEYWORDS}],
)
app.add_page(
    bookmarks_page,
    route="/bookmarks",
    title="Bookmarks — Qualam-e-Hayati",
    description="Your saved reading list, kept privately in this browser.",
    meta=[{"name": "robots", "content": "noindex"}],
)
app.add_page(
    feed_page,
    route="/feed",
    title="Feed & Sitemap — Qualam-e-Hayati",
    description="A chronological feed and sitemap of every piece published in Qualam-e-Hayati.",
    meta=[
        {"name": "keywords", "content": _SITE_KEYWORDS},
        {
            "name": "description",
            "content": "Chronological feed of Qualam-e-Hayati publications.",
        },
    ],
)
app.add_page(
    about_page,
    route="/about",
    title="About — Qualam-e-Hayati",
    description="A quiet literary journal, kept carefully. Read about our editors and principles.",
    meta=[{"name": "keywords", "content": _SITE_KEYWORDS}],
)
app.add_page(
    contact_page,
    route="/contact",
    title="Contact — Qualam-e-Hayati",
    description="Write to Qualam-e-Hayati. Submissions, letters, and correspondence.",
    meta=[{"name": "keywords", "content": _SITE_KEYWORDS}],
)
app.add_page(
    index,
    route="/",
    title="Qualam-e-Hayati — A Literary Journal",
    description="A quiet literary journal for essays, fiction, poetry, and correspondence — printed in light, delivered by evening.",
    meta=[
        {"name": "keywords", "content": _SITE_KEYWORDS},
        {
            "property": "og:title",
            "content": "Qualam-e-Hayati — A Literary Journal",
        },
        {
            "property": "og:description",
            "content": "Essays, fiction, poetry, and quiet correspondence.",
        },
    ],
)
