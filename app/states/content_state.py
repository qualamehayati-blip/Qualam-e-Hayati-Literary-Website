import reflex as rx
from typing import TypedDict


class Publication(TypedDict):
    slug: str
    title: str
    subtitle: str
    author: str
    category: str
    date: str
    year: str
    read_minutes: int
    excerpt: str
    cover_emblem: str
    cover_image: str
    body: list[str]
    body_markdown: str
    tags: list[str]
    status: str
    is_starter: bool


class Category(TypedDict):
    slug: str
    name: str
    urdu: str
    description: str
    count: int
    emblem: str


_PUBLICATIONS: list[Publication] = [
    {
        "slug": "the-lantern-and-the-letter",
        "title": "The Lantern and the Letter",
        "subtitle": "On writing by the light of an unquiet century",
        "author": "Mp Kumawat",
        "category": "Essays",
        "date": "March 14, 2025",
        "year": "2025",
        "read_minutes": 9,
        "excerpt": "There is a lantern in every letter — a small persistent fire that refuses to be edited into silence. This essay traces the private grammar of grief and the quiet architecture of hope.",
        "cover_emblem": "feather",
        "tags": ["memory", "language", "hope"],
        "body": [
            "There is a lantern in every letter. A small, persistent fire that refuses to be edited into silence. When I began keeping a notebook again, after the years that had left me nearly speechless, I did not know that this was the wick I was trimming, night after night.",
            "The century has been unquiet. It has asked our sentences to carry more than sentences were built to carry: a country, a mother tongue, a name pronounced correctly for the first time in a decade. And still we write. We write the way people build shelters — slowly, from what the wind has spared.",
            "My grandmother wrote her letters in a hand so careful it looked like prayer laid down in ink. She addressed her envelopes with the patience of someone who believed that the postman was also a witness. I have inherited neither her patience nor her belief, but I have inherited the lantern.",
            "To write, in this century, is to insist that a private grammar of grief can still be spoken aloud in public rooms. It is to trust that the reader — that unknown, tender, difficult stranger — will lean toward the flame rather than blow it out.",
            "And when I fail, as I often do, I return to the letter. A single letter. The one that stands, small and stubborn, at the beginning of a word I have not yet finished writing.",
        ],
    },
    {
        "slug": "an-orchard-in-october",
        "title": "An Orchard in October",
        "subtitle": "A short story of returning",
        "author": "Mp Kumawat",
        "category": "Fiction",
        "date": "February 2, 2025",
        "year": "2025",
        "read_minutes": 14,
        "excerpt": "He had not walked the orchard in twenty-one autumns. The trees, he discovered, had kept his counsel; the fruit had not.",
        "cover_emblem": "tree-pine",
        "tags": ["memory", "family", "return"],
        "body": [
            "He had not walked the orchard in twenty-one autumns. The trees, he discovered, had kept his counsel; the fruit had not. Every apple that had fallen in his absence had left a small dark coin in the grass, and the grass, being loyal, had grown around each one.",
            "His mother met him at the gate with a cup of tea and a look that had been rehearsed for years and abandoned at the last moment. 'You are late,' she said, which was not an accusation but a fact, the way one might say the moon is full.",
            "In the kitchen, the clock ticked with the same small stubbornness. He recognised the tone of it before he recognised the shape of his own chair. He sat down and the chair sighed, as though it too had been waiting.",
            "Later, in the orchard, she walked ahead of him. She was smaller than he remembered, and the trees were taller. This was, he thought, the arithmetic of leaving: whatever you subtract from a place, the place adds back to itself, quietly, without you.",
            "'The Ambri gave a good crop this year,' she said, touching a low branch. 'It was waiting for someone to notice.'",
            "He did not answer. He put his hand on the bark, which was warm from the last sun, and he understood — with the terrible late clarity that returns bring — that he had come home not to be forgiven but to be counted.",
        ],
    },
    {
        "slug": "ghazal-for-a-borrowed-city",
        "title": "Ghazal for a Borrowed City",
        "subtitle": "Five couplets on exile and evening light",
        "author": "Mp Kumawat",
        "category": "Poetry",
        "date": "January 20, 2025",
        "year": "2025",
        "read_minutes": 3,
        "excerpt": "The city was not mine, but the evenings were — and the evenings, in the end, are what the heart keeps.",
        "cover_emblem": "moon-star",
        "tags": ["exile", "evening", "ghazal"],
        "body": [
            "The city was not mine, but the evenings were.\nAnd the evenings, in the end, are what the heart keeps.",
            "I borrowed a lamp from a stranger's window,\nand walked home under a sky that had learned my name.",
            "Do not ask me where I am from — ask instead\nwhich rain I have stood inside without an umbrella.",
            "The river here answers to a different word,\nbut it still knows how to carry a paper boat.",
            "Farah, if you must leave, leave the way an evening leaves —\nslowly, with a little gold behind it.",
        ],
    },
    {
        "slug": "notes-on-translating-silence",
        "title": "Notes on Translating Silence",
        "subtitle": "The impossible labour of the second language",
        "author": "Mp Kumawat",
        "category": "Essays",
        "date": "December 11, 2024",
        "year": "2024",
        "read_minutes": 11,
        "excerpt": "A translator's silences are not empty. They are the small verandas where the original poem sits down for a moment to catch its breath before continuing in a new tongue.",
        "cover_emblem": "book-open",
        "tags": ["translation", "language", "craft"],
        "body": [
            "A translator's silences are not empty. They are the small verandas where the original poem sits down for a moment to catch its breath before continuing in a new tongue.",
            "There is a word in Urdu — intezaar — which English can only approach from a great distance, waving. 'Waiting' is a plain, useful word, but it does not know how to sit on a doorstep with a cup of tea for forty years.",
            "When I translate, I am not moving a poem from one house to another. I am moving it from one climate to another. The furniture will need to be rearranged. The window will need to face a different weather.",
            "The best translations, I think, are the ones that keep a little of the original silence intact — the small unlit corner where the reader is invited to bring their own lamp.",
        ],
    },
    {
        "slug": "the-conversation-with-mahtab-rizvi",
        "title": "A Conversation with Mahtab Rizvi",
        "subtitle": "On the poetics of the everyday",
        "author": "Mp Kumawat",
        "category": "Interviews",
        "date": "November 3, 2024",
        "year": "2024",
        "read_minutes": 12,
        "excerpt": "The poet speaks of kitchens, of buses, of the small furniture of daily life — and of why the epic, if it is to matter, must be written on a folding table.",
        "cover_emblem": "message-square-quote",
        "tags": ["interview", "poetry", "craft"],
        "body": [
            "Mahtab Rizvi meets me in a tea-house that smells faintly of cardamom and old paper. She is early, which she says is a habit of the anxious and the devout, and she is uncertain which of the two she belongs to today.",
            "'I have never been interested in the epic,' she says, stirring her tea in slow, considered circles. 'Or rather — I am interested in the epic only when it agrees to be written on a folding table. When it agrees to be interrupted by the kettle.'",
            "We speak, for a while, of kitchens. She has a poem — you may know it — about a woman peeling an orange with the patience of a mapmaker. 'The orange is the country,' she says, and then laughs. 'Or the orange is the orange. I have stopped insisting.'",
            "Later, when I ask her what she would tell a young poet, she is quiet for a long time. 'Do not be in a hurry to be understood,' she says finally. 'Be in a hurry to be honest. Understanding, if it comes, will come later — and it will come from a stranger, at an odd hour, and it will feel like being handed back your own coat in the rain.'",
        ],
    },
    {
        "slug": "a-brief-history-of-margins",
        "title": "A Brief History of Margins",
        "subtitle": "On the reader's pencil and the writer's grace",
        "author": "Mp Kumawat",
        "category": "Essays",
        "date": "September 18, 2024",
        "year": "2024",
        "read_minutes": 7,
        "excerpt": "A margin is the small country where the reader is allowed to speak back. It is the writer's most generous act — to leave that country undefended.",
        "cover_emblem": "pen-line",
        "tags": ["reading", "books", "craft"],
        "body": [
            "A margin is the small country where the reader is allowed to speak back. It is the writer's most generous act — to leave that country undefended.",
            "I inherited a copy of Ghalib from a great-uncle whose margins were more argumentative than the poems themselves. He disagreed with Ghalib in three languages, and agreed with him in a fourth that only he understood.",
            "The book, when I first opened it, felt like a room in which two people were still talking. I have not, in the years since, been able to close the door on that conversation. I have only added my own chair.",
            "Every book that is truly loved is, in the end, a co-authored book. The writer provides the weather; the reader provides the umbrella, or refuses one.",
        ],
    },
    {
        "slug": "letter-from-the-editor-winter",
        "title": "Letter from the Editor — Winter",
        "subtitle": "On slowness, on lamps, on beginning again",
        "author": "Mp Kumawat",
        "category": "Letters",
        "date": "December 21, 2024",
        "year": "2024",
        "read_minutes": 4,
        "excerpt": "This winter, we have decided to be slow on purpose. We have decided that the lamp is a kind of argument, and we intend to make it, quietly, all season.",
        "cover_emblem": "mail",
        "tags": ["editorial", "winter"],
        "body": [
            "Dear reader,",
            "This winter, we have decided to be slow on purpose. We have decided that the lamp is a kind of argument, and we intend to make it, quietly, all season. We will publish less; we will publish better. We will ask each piece to earn its place at the table.",
            "You will find, in this issue, a story about an orchard, a ghazal about a borrowed city, and an essay about the small unlit corner of a translated poem. We hope you will read them the way we edited them — with the kettle on, and the door slightly open.",
            "With warmth, and with ink still drying,\n— The Editors",
        ],
    },
    {
        "slug": "the-quiet-craft",
        "title": "The Quiet Craft",
        "subtitle": "A meditation on writing without an audience",
        "author": "Mp Kumawat",
        "category": "Essays",
        "date": "August 5, 2024",
        "year": "2024",
        "read_minutes": 8,
        "excerpt": "There is a kind of writing that is done with the door closed — not against the world, but for the sentence, which is shy and will not come out if it is being watched.",
        "cover_emblem": "feather",
        "tags": ["craft", "solitude"],
        "body": [
            "There is a kind of writing that is done with the door closed — not against the world, but for the sentence, which is shy and will not come out if it is being watched.",
            "I have written, at various times, for money, for approval, for the small clean pleasure of finishing a paragraph before the tea goes cold. But the writing I trust most is the writing I did before I knew anyone was listening — the writing that was, in the truest sense, a rehearsal for a conversation I had not yet been invited to.",
            "The audience, when it arrives, is a gift. But it is not the reason. The reason is the sentence itself, coming forward, at last, to speak.",
        ],
    },
    {
        "slug": "the-cartographer-of-small-kindnesses",
        "title": "The Cartographer of Small Kindnesses",
        "subtitle": "A short story about a man who mapped his neighbourhood's courtesies",
        "author": "Mp Kumawat",
        "category": "Fiction",
        "date": "October 12, 2024",
        "year": "2024",
        "read_minutes": 10,
        "excerpt": "He drew, upon a folded page, the exact spot where the tea-seller left an extra biscuit for the widow, and the corner where the postman waited a moment longer before ringing the bell.",
        "cover_emblem": "map",
        "tags": ["neighbourhood", "kindness", "story"],
        "body": [
            "He drew, upon a folded page, the exact spot where the tea-seller left an extra biscuit for the widow — a small pencilled cross that felt to him more truthful than most of the streets on the municipal map.",
            "There were, he had noticed, two cities laid over one another. The city of addresses, and the city of pauses. He had grown up in the first and only lately learned the second.",
            "By the end of that winter his page was crowded, and the neighbourhood had begun, without knowing it, to lean toward him — the way a room leans, faintly, toward the one lamp still burning at midnight.",
            "When he was asked, later, what he had been doing all those months with the folded page in his pocket, he said: 'Keeping the accounts.' It was, he felt, the closest a sentence could come to the truth without breaking it.",
        ],
    },
    {
        "slug": "nazm-for-a-slow-rain",
        "title": "Nazm for a Slow Rain",
        "subtitle": "A short nazm on patience and the sound of water",
        "author": "Mp Kumawat",
        "category": "Poetry",
        "date": "July 22, 2024",
        "year": "2024",
        "read_minutes": 2,
        "excerpt": "The rain here does not hurry. It falls the way an old letter is read — slowly, with breaks for weeping.",
        "cover_emblem": "cloud-drizzle",
        "tags": ["rain", "nazm", "patience"],
        "body": [
            "The rain here does not hurry.\nIt falls the way an old letter is read —\nslowly, with breaks for weeping.",
            "On the veranda, an aunt keeps count\nof the drops that miss the tulsi pot.\nShe does not tell anyone the number.\nIt is her private currency.",
            "When the rain stops, she will not say the rain has stopped.\nShe will say, 'The sky has finished its errands.'\nAnd we, being polite, will believe her.",
        ],
    },
    {
        "slug": "on-reading-aloud",
        "title": "On Reading Aloud",
        "subtitle": "Why some sentences ask to be spoken",
        "author": "Mp Kumawat",
        "category": "Essays",
        "date": "June 4, 2024",
        "year": "2024",
        "read_minutes": 6,
        "excerpt": "A sentence is not finished until it has been spoken aloud at least once — to a child, a lamp, or the empty chair at the end of the table.",
        "cover_emblem": "volume-2",
        "tags": ["reading", "voice", "craft"],
        "body": [
            "A sentence is not finished until it has been spoken aloud at least once — to a child, a lamp, or the empty chair at the end of the table. Reading is a private act; reading aloud is a small, formal ceremony.",
            "My father read the newspaper aloud each morning, though there was no one in the kitchen but the kettle. He read the way a man tunes a radio — patiently, in search of a frequency the day had not yet chosen.",
            "I think of him now when I read my own drafts aloud. Some sentences duck under the counter. Others walk forward and shake my hand. It is the ones that walk forward I keep.",
        ],
    },
    {
        "slug": "letter-from-the-editor-autumn",
        "title": "Letter from the Editor — Autumn",
        "subtitle": "On what we mean when we say 'season'",
        "author": "Mp Kumawat",
        "category": "Letters",
        "date": "September 30, 2024",
        "year": "2024",
        "read_minutes": 3,
        "excerpt": "The seasons are, more than anything else, a shared piece of furniture. This autumn we have rearranged it slightly, and moved the reading chair closer to the window.",
        "cover_emblem": "mail-open",
        "tags": ["editorial", "autumn"],
        "body": [
            "Dear reader,",
            "The seasons are, more than anything else, a shared piece of furniture. This autumn we have rearranged it slightly — moved the reading chair closer to the window, folded the summer blanket into the trunk beneath the bed.",
            "You will find in these pages a story about a cartographer, a nazm about slow rain, and an essay about the small ceremony of reading aloud. We hope you will keep them for the season, and lend them, if you like, to a friend who has not yet made room for autumn.",
            "With ink still drying,\n— The Editors",
        ],
    },
    {
        "slug": "a-conversation-with-ayaz-sethi",
        "title": "A Conversation with Ayaz Sethi",
        "subtitle": "On writing fiction from the corner of the eye",
        "author": "Mp Kumawat",
        "category": "Interviews",
        "date": "May 18, 2024",
        "year": "2024",
        "read_minutes": 11,
        "excerpt": "The novelist speaks of peripheral vision, of the characters who arrive quietly, and of why he has never trusted a story that announces itself at the door.",
        "cover_emblem": "message-square-quote",
        "tags": ["interview", "fiction", "craft"],
        "body": [
            "Ayaz Sethi lives on the top floor of a house that leans, very slightly, toward the west. He answers the door with the air of a man interrupted mid-sentence, which is, he explains, the only air he has.",
            "'I have never trusted a story that announces itself at the door,' he says, pouring tea with the patience of someone who has done it, in the same cup, for thirty years. 'The good ones arrive by the side entrance. Sometimes they are already in the kitchen before I have noticed.'",
            "We speak, for a while, of peripheral vision. He describes an old habit — jotting down, each evening, the smallest thing he saw that day that no one had told him to see. 'A pigeon,' he says. 'A green bucket. The particular tiredness of a woman waiting for a bus.'",
            "'That is the whole craft,' he says at last. 'Everything else is furniture.'",
        ],
    },
    {
        "slug": "the-weight-of-a-postcard",
        "title": "The Weight of a Postcard",
        "subtitle": "A story about what a small paper can carry",
        "author": "Mp Kumawat",
        "category": "Fiction",
        "date": "April 9, 2024",
        "year": "2024",
        "read_minutes": 9,
        "excerpt": "She had kept the postcard for forty-one years. It weighed almost nothing, and yet each time she moved houses it was the first thing she packed.",
        "cover_emblem": "send",
        "tags": ["memory", "letters", "story"],
        "body": [
            "She had kept the postcard for forty-one years. It weighed almost nothing, and yet each time she moved houses it was the first thing she packed — before the china, before the wedding photograph, before the small silver box that held her mother's earrings.",
            "The message on the back was six words long. She had read them so many times that they had stopped being sentences and become, instead, a kind of small weather system in the room where she read them.",
            "When her granddaughter finally asked her what the postcard said, she thought for a long moment. 'It says,' she answered, 'that I was, once, thought of.' And then she laughed, softly, because she had been thought of many times since, and none of them, somehow, had ever needed a stamp.",
        ],
    },
    {
        "slug": "the-library-at-the-end-of-the-lane",
        "title": "The Library at the End of the Lane",
        "subtitle": "On the small public rooms that raised us",
        "author": "Mp Kumawat",
        "category": "Essays",
        "date": "February 14, 2024",
        "year": "2024",
        "read_minutes": 7,
        "excerpt": "There was a library at the end of the lane. It had three good chairs, a broken clock, and a librarian who believed that every reader deserved to be greeted by name.",
        "cover_emblem": "library",
        "tags": ["libraries", "childhood", "reading"],
        "body": [
            "There was a library at the end of the lane. It had three good chairs, a broken clock, and a librarian who believed that every reader — no matter how small, no matter how often they returned the book late — deserved to be greeted by name.",
            "I learned, in that room, what a room can teach. Silence, for instance. And the etiquette of turning a page slowly, out of respect for the person beside you who was three pages behind.",
            "The library is gone now. In its place there is a shop that sells mobile phone accessories, cheerfully, all day. I do not blame the shop. I only blame myself, sometimes, for not knowing — at the time — that some rooms are not permanent, and must be memorised while one is still inside them.",
        ],
    },
]


_CATEGORIES: list[Category] = [
    {
        "slug": "essays",
        "name": "Essays",
        "urdu": "مضامین",
        "description": "Long-form reflections on language, memory, and the quiet architecture of daily life.",
        "count": 6,
        "emblem": "feather",
    },
    {
        "slug": "fiction",
        "name": "Fiction",
        "urdu": "افسانہ",
        "description": "Short stories that hold a small lamp to the corners of a familiar room.",
        "count": 3,
        "emblem": "book-open",
    },
    {
        "slug": "poetry",
        "name": "Poetry",
        "urdu": "شاعری",
        "description": "Ghazals, nazms, and verses attentive to the evening light of a borrowed century.",
        "count": 2,
        "emblem": "moon-star",
    },
    {
        "slug": "interviews",
        "name": "Interviews",
        "urdu": "مکالمہ",
        "description": "Conversations with writers who have made a home in the sentence.",
        "count": 2,
        "emblem": "message-square-quote",
    },
    {
        "slug": "letters",
        "name": "Letters",
        "urdu": "خط",
        "description": "Editorial letters, notes from readers, and correspondence that keeps the fire lit.",
        "count": 2,
        "emblem": "mail",
    },
]


# Normalize new fields on seed data — every seeded piece is a starter
# sample. Mp Kumawat can clear these from the editorial desk once his
# own writing has taken their place.
for _p in _PUBLICATIONS:
    _p.setdefault("status", "published")
    _p.setdefault("cover_image", "")
    _p.setdefault("body_markdown", "")
    _p["is_starter"] = True


class ContentState(rx.State):
    publications: list[Publication] = _PUBLICATIONS
    categories: list[Category] = _CATEGORIES

    # Reader tools: search / filter / pagination
    search_query: str = ""
    filter_category: str = "All"
    filter_year: str = "All"
    current_page: int = 1
    page_size: int = 6

    @rx.event
    def set_search(self, q: str):
        self.search_query = q
        self.current_page = 1

    @rx.event
    def set_filter_category(self, c: str):
        self.filter_category = c
        self.current_page = 1

    @rx.event
    def set_filter_year(self, y: str):
        self.filter_year = y
        self.current_page = 1

    @rx.event
    def clear_filters(self):
        self.search_query = ""
        self.filter_category = "All"
        self.filter_year = "All"
        self.current_page = 1

    @rx.event
    def go_next_page(self):
        total = self.total_pages
        if self.current_page < total:
            self.current_page += 1
            return rx.call_script(
                "window.scrollTo({top: 0, behavior: 'smooth'})"
            )

    @rx.event
    def go_prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            return rx.call_script(
                "window.scrollTo({top: 0, behavior: 'smooth'})"
            )

    @rx.event
    def share_current(self):
        return [
            rx.call_script(
                "navigator.clipboard && navigator.clipboard.writeText(window.location.href)"
            ),
            rx.toast("Link copied to your clipboard.", duration=2500),
        ]

    @rx.var
    def available_years(self) -> list[str]:
        seen: list[str] = []
        for p in self.publications:
            if p["year"] not in seen:
                seen.append(p["year"])
        seen.sort(reverse=True)
        return seen

    @rx.var
    def category_names(self) -> list[str]:
        return [c["name"] for c in self.categories]

    @rx.var
    def starter_count(self) -> int:
        return sum(1 for p in self.publications if p.get("is_starter"))

    @rx.var
    def has_starter_content(self) -> bool:
        return self.starter_count > 0

    @rx.var
    def public_publications(self) -> list[Publication]:
        return [
            p
            for p in self.publications
            if p.get("status", "published") == "published"
        ]

    @rx.var
    def filtered_publications(self) -> list[Publication]:
        q = self.search_query.strip().lower()
        result = self.public_publications
        if self.filter_category != "All":
            result = [
                p for p in result if p["category"] == self.filter_category
            ]
        if self.filter_year != "All":
            result = [p for p in result if p["year"] == self.filter_year]
        if q:

            @rx.event
            def matches(p: Publication) -> bool:
                if q in p["title"].lower() or q in p["subtitle"].lower():
                    return True
                if q in p["excerpt"].lower() or q in p["author"].lower():
                    return True
                if q in p["category"].lower():
                    return True
                for t in p["tags"]:
                    if q in t.lower():
                        return True
                return False

            result = [p for p in result if matches(p)]
        return result

    @rx.var
    def results_count(self) -> int:
        return len(self.filtered_publications)

    @rx.var
    def total_pages(self) -> int:
        n = len(self.filtered_publications)
        if n == 0:
            return 1
        return (n + self.page_size - 1) // self.page_size

    @rx.var
    def paginated_publications(self) -> list[Publication]:
        start = (self.current_page - 1) * self.page_size
        return self.filtered_publications[start : start + self.page_size]

    @rx.var
    def has_prev_page(self) -> bool:
        return self.current_page > 1

    @rx.var
    def has_next_page(self) -> bool:
        return self.current_page < self.total_pages

    @rx.var
    def has_active_filters(self) -> bool:
        return (
            self.search_query != ""
            or self.filter_category != "All"
            or self.filter_year != "All"
        )

    @rx.var
    def current_index(self) -> int:
        slug = self.router.page.params.get("slug", "")
        pubs = self.public_publications
        for i, p in enumerate(pubs):
            if p["slug"] == slug:
                return i
        return -1

    @rx.var
    def prev_publication(self) -> Publication:
        idx = self.current_index
        pubs = self.public_publications
        if idx > 0:
            return pubs[idx - 1]
        return self._empty_publication()

    @rx.var
    def next_publication(self) -> Publication:
        idx = self.current_index
        pubs = self.public_publications
        if 0 <= idx < len(pubs) - 1:
            return pubs[idx + 1]
        return self._empty_publication()

    @rx.var
    def has_prev_article(self) -> bool:
        return self.current_index > 0

    @rx.var
    def has_next_article(self) -> bool:
        idx = self.current_index
        return 0 <= idx < len(self.public_publications) - 1

    def _empty_publication(self) -> Publication:
        return {
            "slug": "",
            "title": "",
            "subtitle": "",
            "author": "",
            "category": "",
            "date": "",
            "year": "",
            "read_minutes": 0,
            "excerpt": "",
            "cover_emblem": "book",
            "cover_image": "",
            "body": [],
            "body_markdown": "",
            "tags": [],
            "status": "published",
            "is_starter": False,
        }

    @rx.var
    def featured(self) -> Publication:
        pubs = self.public_publications
        if len(pubs) > 0:
            return pubs[0]
        return self._empty_publication()

    @rx.var
    def latest(self) -> list[Publication]:
        return self.public_publications[1:4]

    @rx.var
    def more(self) -> list[Publication]:
        return self.public_publications[4:]

    @rx.var
    def all_publications(self) -> list[Publication]:
        return self.public_publications

    @rx.var
    def current_slug(self) -> str:
        return self.router.page.params.get("slug", "")

    @rx.var
    def current_publication(self) -> Publication:
        slug = self.router.page.params.get("slug", "")
        for pub in self.publications:
            if pub["slug"] == slug:
                return pub
        return {
            "slug": "",
            "title": "Not found",
            "subtitle": "This piece has wandered off the page.",
            "author": "—",
            "category": "—",
            "date": "",
            "year": "",
            "read_minutes": 0,
            "excerpt": "",
            "cover_emblem": "book",
            "cover_image": "",
            "body": [
                "The piece you are looking for could not be found. Perhaps it is still being written."
            ],
            "body_markdown": "",
            "tags": [],
            "status": "published",
            "is_starter": False,
        }

    @rx.var
    def current_category_slug(self) -> str:
        return self.router.page.params.get("slug", "")

    @rx.var
    def current_category(self) -> Category:
        slug = self.router.page.params.get("slug", "")
        for cat in self.categories:
            if cat["slug"] == slug:
                return cat
        return {
            "slug": "",
            "name": "All Writing",
            "urdu": "",
            "description": "Every piece in the journal.",
            "count": len(self.publications),
            "emblem": "book",
        }

    @rx.var
    def current_category_publications(self) -> list[Publication]:
        slug = self.router.page.params.get("slug", "")
        target = ""
        for cat in self.categories:
            if cat["slug"] == slug:
                target = cat["name"]
                break
        pubs = self.public_publications
        if not target:
            return pubs
        return [p for p in pubs if p["category"] == target]
