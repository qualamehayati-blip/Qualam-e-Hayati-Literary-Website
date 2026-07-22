import reflex as rx
import re
import logging
from app.states.content_state import ContentState, Publication, Category
from app.states.auth_state import AuthState


_EMBLEM_OPTIONS: list[str] = [
    "feather",
    "book-open",
    "moon-star",
    "message-square-quote",
    "mail",
    "mail-open",
    "tree-pine",
    "cloud-drizzle",
    "map",
    "library",
    "pen-line",
    "send",
    "volume-2",
    "star",
    "sun",
    "flame",
    "quote",
]


class AdminState(rx.State):
    """State for admin editing forms and CRUD event handlers.

    The public event handlers each gate on `AuthState.is_authenticated`
    and mutate `ContentState.publications` / `ContentState.categories`
    via the framework's `self.get_state(...)` accessor.

    All mutation logic is factored into leading-underscore helper
    methods (`_apply_*_to_content`) that accept a `ContentState`
    instance directly. This is the app's declared backend-only test
    seam: unit tests can construct a fresh `AdminState(**form_kwargs)`
    and a fresh `ContentState()` and drive the pure CRUD logic without
    going through Reflex's substate resolver, while production code
    always reaches these helpers behind an authenticated event
    handler.

    Construction from tests
    """

    # ---------- Publication form ----------
    editing_slug: str = ""
    form_title: str = ""
    form_subtitle: str = ""
    form_author: str = "Mp Kumawat"
    form_category: str = "Essays"
    form_date: str = ""
    form_year: str = ""
    form_read_minutes: int = 5
    form_excerpt: str = ""
    form_cover_emblem: str = "feather"
    form_cover_image: str = ""
    form_tags: str = ""
    form_body_markdown: str = ""
    form_status: str = "draft"
    preview_mode: bool = False

    # ---------- Category form ----------
    cat_editing_slug: str = ""
    cat_form_slug: str = ""
    cat_form_name: str = ""
    cat_form_urdu: str = ""
    cat_form_description: str = ""
    cat_form_emblem: str = "book-open"

    # ---------- Dashboard filter ----------
    dashboard_filter: str = "all"  # all | published | draft
    dashboard_search: str = ""

    @rx.var
    def emblem_options(self) -> list[str]:
        return _EMBLEM_OPTIONS

    # -----------------------------------------------------------------
    # Auth gates + on_load handlers
    # -----------------------------------------------------------------
    @rx.event
    async def require_admin(self):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")

    @rx.event
    async def load_new_form(self):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")
        self._reset_pub_form()

    @rx.event
    async def load_edit_form(self):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")
        slug = self.router.page.params.get("slug", "")
        content = await self.get_state(ContentState)
        for p in content.publications:
            if p["slug"] == slug:
                self.editing_slug = slug
                self.form_title = p["title"]
                self.form_subtitle = p["subtitle"]
                self.form_author = p["author"] or "Mp Kumawat"
                self.form_category = p["category"]
                self.form_date = p["date"]
                self.form_year = p["year"]
                self.form_read_minutes = p["read_minutes"]
                self.form_excerpt = p["excerpt"]
                self.form_cover_emblem = p["cover_emblem"]
                self.form_cover_image = p.get("cover_image", "")
                self.form_tags = ", ".join(p["tags"])
                self.form_body_markdown = p.get(
                    "body_markdown", ""
                ) or "\n\n".join(p["body"])
                self.form_status = p.get("status", "published")
                self.preview_mode = False
                return
        self._reset_pub_form()

    def _reset_pub_form(self):
        self.editing_slug = ""
        self.form_title = ""
        self.form_subtitle = ""
        self.form_author = "Mp Kumawat"
        self.form_category = "Essays"
        self.form_date = ""
        self.form_year = ""
        self.form_read_minutes = 5
        self.form_excerpt = ""
        self.form_cover_emblem = "feather"
        self.form_cover_image = ""
        self.form_tags = ""
        self.form_body_markdown = ""
        self.form_status = "draft"
        self.preview_mode = False

    # -----------------------------------------------------------------
    # Controlled field setters for the publication editor
    # -----------------------------------------------------------------
    @rx.event
    def set_form_title(self, v: str):
        self.form_title = v

    @rx.event
    def set_form_subtitle(self, v: str):
        self.form_subtitle = v

    @rx.event
    def set_form_author(self, v: str):
        self.form_author = v

    @rx.event
    def set_form_category(self, v: str):
        self.form_category = v

    @rx.event
    def set_form_date(self, v: str):
        self.form_date = v

    @rx.event
    def set_form_year(self, v: str):
        self.form_year = v

    @rx.event
    def set_form_read_minutes(self, v: float):
        try:
            self.form_read_minutes = max(1, int(v or 1))
        except Exception as e:
            logging.exception(f"Invalid read_minutes: {e}")
            self.form_read_minutes = 5

    @rx.event
    def set_form_excerpt(self, v: str):
        self.form_excerpt = v

    @rx.event
    def set_form_cover_emblem(self, v: str):
        self.form_cover_emblem = v

    @rx.event
    def set_form_cover_image(self, v: str):
        self.form_cover_image = v

    @rx.event
    def set_form_tags(self, v: str):
        self.form_tags = v

    @rx.event
    def set_form_body_markdown(self, v: str):
        self.form_body_markdown = v

    @rx.event
    def set_form_status(self, v: str):
        self.form_status = v if v in ("draft", "published") else "draft"

    @rx.event
    def toggle_preview(self):
        self.preview_mode = not self.preview_mode

    @rx.event
    def insert_snippet(self, snippet: str):
        sep = "\n\n" if self.form_body_markdown.strip() else ""
        self.form_body_markdown = f"{self.form_body_markdown}{sep}{snippet}"

    # -----------------------------------------------------------------
    # Dashboard filter
    # -----------------------------------------------------------------
    @rx.event
    def set_dashboard_filter(self, v: str):
        self.dashboard_filter = (
            v if v in ("all", "published", "draft") else "all"
        )

    @rx.event
    def set_dashboard_search(self, v: str):
        self.dashboard_search = v

    @rx.var
    async def dashboard_publications(self) -> list[Publication]:
        content = await self.get_state(ContentState)
        items = list(content.publications)
        if self.dashboard_filter == "published":
            items = [p for p in items if p.get("status") == "published"]
        elif self.dashboard_filter == "draft":
            items = [p for p in items if p.get("status") == "draft"]
        q = self.dashboard_search.strip().lower()
        if q:
            items = [
                p
                for p in items
                if q in p["title"].lower()
                or q in p["author"].lower()
                or q in p["category"].lower()
            ]
        return items

    @rx.var
    async def total_publications(self) -> int:
        content = await self.get_state(ContentState)
        return len(content.publications)

    @rx.var
    async def total_published(self) -> int:
        content = await self.get_state(ContentState)
        return sum(
            1 for p in content.publications if p.get("status") == "published"
        )

    @rx.var
    async def total_drafts(self) -> int:
        content = await self.get_state(ContentState)
        return sum(
            1 for p in content.publications if p.get("status") == "draft"
        )

    @rx.var
    async def total_categories(self) -> int:
        content = await self.get_state(ContentState)
        return len(content.categories)

    @rx.var
    async def has_starter_content(self) -> bool:
        content = await self.get_state(ContentState)
        return any(p.get("is_starter") for p in content.publications)

    @rx.var
    async def starter_count(self) -> int:
        content = await self.get_state(ContentState)
        return sum(1 for p in content.publications if p.get("is_starter"))

    @rx.var
    async def own_publication_count(self) -> int:
        content = await self.get_state(ContentState)
        return sum(1 for p in content.publications if not p.get("is_starter"))

    # -----------------------------------------------------------------
    # Pure helpers (declared test seam) — mutate a ContentState passed in
    # -----------------------------------------------------------------
    def _slugify(self, s: str) -> str:
        s = s.lower().strip()
        s = re.sub(r"[^a-z0-9\s-]", "", s)
        s = re.sub(r"[\s_-]+", "-", s)
        return s.strip("-") or "untitled"

    def _unique_slug(self, base: str, existing: list[str]) -> str:
        if base not in existing:
            return base
        i = 2
        while f"{base}-{i}" in existing:
            i += 1
        return f"{base}-{i}"

    def _recount_categories(self, content: ContentState) -> None:
        new_cats: list[Category] = []
        for cat in content.categories:
            c: Category = {
                "slug": cat["slug"],
                "name": cat["name"],
                "urdu": cat["urdu"],
                "description": cat["description"],
                "emblem": cat["emblem"],
                "count": sum(
                    1
                    for p in content.publications
                    if p["category"] == cat["name"]
                    and p.get("status") == "published"
                ),
            }
            new_cats.append(c)
        content.categories = new_cats

    async def _apply_save_publication_to_content(
        self, content: ContentState, publish: bool = False
    ) -> tuple[bool, str, str]:
        """Save/update a publication on the given ContentState.

        Returns (ok, slug, message). Public event handlers call this
        after checking auth; unit tests call it directly.
        """
        title = self.form_title.strip()
        if not title:
            return (False, "", "A title is required to save.")
        if not self.form_body_markdown.strip():
            return (
                False,
                "",
                "The body cannot be empty — even a single line will do.",
            )

        body_paragraphs = [
            b.strip()
            for b in re.split(r"\n\s*\n", self.form_body_markdown.strip())
            if b.strip()
        ]
        tags = [t.strip() for t in self.form_tags.split(",") if t.strip()]

        status_now = "published" if publish else self.form_status
        if status_now not in ("draft", "published"):
            status_now = "draft"

        if self.editing_slug:
            slug = self.editing_slug
            # Preserve the original starter flag when editing an
            # existing seeded piece; new pieces authored by
            # Mp Kumawat are always marked as his own work.
            is_starter = False
            for p in content.publications:
                if p["slug"] == slug:
                    is_starter = bool(p.get("is_starter", False))
                    break
        else:
            existing = [p["slug"] for p in content.publications]
            slug = self._unique_slug(self._slugify(title), existing)
            is_starter = False

        pub: Publication = {
            "slug": slug,
            "title": title,
            "subtitle": self.form_subtitle.strip(),
            "author": self.form_author.strip() or "Mp Kumawat",
            "category": self.form_category or "Essays",
            "date": self.form_date.strip(),
            "year": (self.form_year.strip() or self.form_date.strip()[:4])
            or "",
            "read_minutes": max(1, int(self.form_read_minutes or 1)),
            "excerpt": self.form_excerpt.strip(),
            "cover_emblem": self.form_cover_emblem or "feather",
            "cover_image": self.form_cover_image.strip(),
            "body": body_paragraphs,
            "body_markdown": self.form_body_markdown,
            "tags": tags,
            "status": status_now,
            "is_starter": is_starter,
        }

        replaced = False
        new_list: list[Publication] = []
        for p in content.publications:
            if p["slug"] == slug and self.editing_slug:
                new_list.append(pub)
                replaced = True
            else:
                new_list.append(p)
        if not replaced:
            new_list.insert(0, pub)
        content.publications = new_list
        self._recount_categories(content)

        self.editing_slug = slug
        self.form_status = status_now

        msg = (
            "Published to the journal."
            if status_now == "published"
            else "Draft saved to your desk."
        )
        return (True, slug, msg)

    async def _apply_delete_publication_to_content(
        self, content: ContentState, slug: str
    ) -> None:
        content.publications = [
            p for p in content.publications if p["slug"] != slug
        ]
        self._recount_categories(content)

    async def _apply_toggle_publish_to_content(
        self, content: ContentState, slug: str
    ) -> str:
        new_list: list[Publication] = []
        msg = "Status updated."
        for p in content.publications:
            if p["slug"] == slug:
                q = dict(p)
                q["status"] = (
                    "draft" if p.get("status") == "published" else "published"
                )
                msg = (
                    "Piece published."
                    if q["status"] == "published"
                    else "Moved to drafts."
                )
                new_list.append(q)  # type: ignore
            else:
                new_list.append(p)
        content.publications = new_list
        self._recount_categories(content)
        return msg

    async def _apply_clear_starter_content(self, content: ContentState) -> int:
        removed = sum(1 for p in content.publications if p.get("is_starter"))
        content.publications = [
            p for p in content.publications if not p.get("is_starter")
        ]
        self._recount_categories(content)
        return removed

    async def _apply_save_category_to_content(
        self, content: ContentState
    ) -> tuple[bool, str]:
        name = self.cat_form_name.strip()
        if not name:
            return (False, "Category name is required.")

        emblem = self.cat_form_emblem or "book-open"
        description = self.cat_form_description.strip()
        urdu = self.cat_form_urdu.strip()

        if self.cat_editing_slug:
            old_name = ""
            for c in content.categories:
                if c["slug"] == self.cat_editing_slug:
                    old_name = c["name"]
                    break
            new_cats: list[Category] = []
            for c in content.categories:
                if c["slug"] == self.cat_editing_slug:
                    new_cats.append(
                        {
                            "slug": c["slug"],
                            "name": name,
                            "urdu": urdu,
                            "description": description,
                            "emblem": emblem,
                            "count": c["count"],
                        }
                    )
                else:
                    new_cats.append(c)
            content.categories = new_cats
            if old_name and old_name != name:
                new_pubs: list[Publication] = []
                for p in content.publications:
                    if p["category"] == old_name:
                        q = dict(p)
                        q["category"] = name
                        new_pubs.append(q)  # type: ignore
                    else:
                        new_pubs.append(p)
                content.publications = new_pubs
            msg = "Category updated."
        else:
            slug = self._slugify(name)
            existing = [c["slug"] for c in content.categories]
            slug = self._unique_slug(slug, existing)
            content.categories = content.categories + [
                {
                    "slug": slug,
                    "name": name,
                    "urdu": urdu,
                    "description": description,
                    "emblem": emblem,
                    "count": 0,
                }
            ]
            msg = "Category created."

        self._recount_categories(content)
        self._reset_cat_form()
        return (True, msg)

    async def _apply_delete_category_to_content(
        self, content: ContentState, slug: str
    ) -> tuple[bool, str]:
        target_name = ""
        for c in content.categories:
            if c["slug"] == slug:
                target_name = c["name"]
                break
        in_use = sum(
            1 for p in content.publications if p["category"] == target_name
        )
        if in_use > 0:
            return (
                False,
                f"Cannot delete — {in_use} piece(s) still live in this section.",
            )
        content.categories = [
            c for c in content.categories if c["slug"] != slug
        ]
        if self.cat_editing_slug == slug:
            self._reset_cat_form()
        return (True, "Category removed.")

    # -----------------------------------------------------------------
    # Publication CRUD event handlers (auth-gated)
    # -----------------------------------------------------------------
    @rx.event
    async def save_publication(self, publish: bool = False):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")
        content = await self.get_state(ContentState)
        ok, _slug, msg = await self._apply_save_publication_to_content(
            content, publish=publish
        )
        if not ok:
            return rx.toast(msg, duration=2800)
        return [rx.toast(msg, duration=2200), rx.redirect("/admin")]

    @rx.event
    async def save_draft(self):
        self.form_status = "draft"
        yield AdminState.save_publication(False)

    @rx.event
    async def publish_now(self):
        self.form_status = "published"
        yield AdminState.save_publication(True)

    @rx.event
    async def toggle_publish(self, slug: str):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")
        content = await self.get_state(ContentState)
        msg = await self._apply_toggle_publish_to_content(content, slug)
        return rx.toast(msg, duration=2000)

    @rx.event
    async def delete_publication(self, slug: str):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")
        content = await self.get_state(ContentState)
        await self._apply_delete_publication_to_content(content, slug)
        return rx.toast("Piece removed from the journal.", duration=2200)

    @rx.event
    async def clear_starter_content(self):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")
        content = await self.get_state(ContentState)
        removed = await self._apply_clear_starter_content(content)
        if removed == 0:
            return rx.toast(
                "There is no starter content to clear.", duration=2400
            )
        return rx.toast(
            f"Cleared {removed} starter piece(s). The journal is now yours.",
            duration=2800,
        )

    # -----------------------------------------------------------------
    # Category form + CRUD
    # -----------------------------------------------------------------
    @rx.event
    def set_cat_form_name(self, v: str):
        self.cat_form_name = v

    @rx.event
    def set_cat_form_urdu(self, v: str):
        self.cat_form_urdu = v

    @rx.event
    def set_cat_form_description(self, v: str):
        self.cat_form_description = v

    @rx.event
    def set_cat_form_emblem(self, v: str):
        self.cat_form_emblem = v

    def _reset_cat_form(self) -> None:
        """Plain-Python reset used by helpers; safe to call from tests."""
        self.cat_editing_slug = ""
        self.cat_form_slug = ""
        self.cat_form_name = ""
        self.cat_form_urdu = ""
        self.cat_form_description = ""
        self.cat_form_emblem = "book-open"

    @rx.event
    def start_new_category(self):
        self._reset_cat_form()

    @rx.event
    async def start_edit_category(self, slug: str):
        content = await self.get_state(ContentState)
        for c in content.categories:
            if c["slug"] == slug:
                self.cat_editing_slug = slug
                self.cat_form_slug = slug
                self.cat_form_name = c["name"]
                self.cat_form_urdu = c["urdu"]
                self.cat_form_description = c["description"]
                self.cat_form_emblem = c["emblem"]
                return

    @rx.event
    async def save_category(self):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")
        content = await self.get_state(ContentState)
        ok, msg = await self._apply_save_category_to_content(content)
        return rx.toast(msg, duration=2200)

    @rx.event
    async def delete_category(self, slug: str):
        auth = await self.get_state(AuthState)
        if not auth.is_authenticated:
            return rx.redirect("/admin/login")
        content = await self.get_state(ContentState)
        ok, msg = await self._apply_delete_category_to_content(content, slug)
        return rx.toast(msg, duration=3000 if not ok else 2000)
