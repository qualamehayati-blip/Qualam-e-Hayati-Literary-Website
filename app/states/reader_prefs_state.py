import reflex as rx
import json
import logging
from app.states.content_state import ContentState, Publication


class ReaderPrefsState(rx.State):
    """Reader preferences persisted to browser LocalStorage.

    Stores reader theme, font-size level, and bookmarked publication slugs.
    """

    theme: str = rx.LocalStorage("light", name="qeh_reader_theme", sync=True)
    font_size: str = rx.LocalStorage("md", name="qeh_reader_font", sync=True)
    bookmarks_json: str = rx.LocalStorage("[]", name="qeh_bookmarks", sync=True)

    @rx.var
    def bookmarks(self) -> list[str]:
        try:
            data = json.loads(self.bookmarks_json or "[]")
            if isinstance(data, list):
                return [str(x) for x in data]
            return []
        except Exception as e:
            logging.exception(f"Failed to parse bookmarks: {e}")
            return []

    @rx.var
    def bookmark_count(self) -> int:
        return len(self.bookmarks)

    @rx.var
    async def bookmarked_publications(self) -> list[Publication]:
        content = await self.get_state(ContentState)
        marks = set(self.bookmarks)
        return [p for p in content.publications if p["slug"] in marks]

    @rx.event
    def toggle_bookmark(self, slug: str):
        current = self.bookmarks
        if slug in current:
            current.remove(slug)
            self.bookmarks_json = json.dumps(current)
            return rx.toast("Removed from your reading list.", duration=2000)
        current.append(slug)
        self.bookmarks_json = json.dumps(current)
        return rx.toast("Saved to your reading list.", duration=2000)

    @rx.event
    def clear_bookmarks(self):
        self.bookmarks_json = "[]"
        return rx.toast("Reading list cleared.", duration=2000)

    @rx.event
    def set_theme(self, theme: str):
        self.theme = theme if theme in ("light", "dark") else "light"

    @rx.event
    def toggle_theme(self):
        self.theme = "dark" if self.theme == "light" else "light"

    @rx.event
    def set_font_size(self, size: str):
        self.font_size = size if size in ("sm", "md", "lg") else "md"
