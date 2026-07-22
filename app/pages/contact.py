import reflex as rx
from app.components.layout import layout
from app.states.contact_state import ContactState


def _field(
    label: str, name: str, placeholder: str, input_type: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="block font-mono-caps text-[0.65rem] text-[#6b6558] mb-2",
        ),
        rx.el.input(
            type=input_type,
            name=name,
            placeholder=placeholder,
            required=True,
            class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-4 py-3 text-[#1f2422] font-serif-body text-[0.98rem] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 placeholder:text-[#a89f8a]",
        ),
        class_name="mb-6",
    )


def _textarea(label: str, name: str, placeholder: str) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="block font-mono-caps text-[0.65rem] text-[#6b6558] mb-2",
        ),
        rx.el.textarea(
            name=name,
            placeholder=placeholder,
            required=True,
            rows="7",
            class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-4 py-3 text-[#1f2422] font-serif-body text-[0.98rem] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 placeholder:text-[#a89f8a] resize-none",
        ),
        class_name="mb-6",
    )


def _info_card(icon: str, title: str, body: str, detail: str) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(icon, size=20, class_name="text-[#244a3c]"),
            class_name="w-12 h-12 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec] mb-4",
        ),
        rx.el.div(title, class_name="font-display text-xl text-[#1f2422] mb-2"),
        rx.el.p(
            body,
            class_name="text-[0.9rem] text-[#3a3f3c] leading-relaxed font-serif-body mb-3",
        ),
        rx.el.div(
            detail, class_name="font-mono-caps text-[0.7rem] text-[#b08b3f]"
        ),
        class_name="paper-card rounded-sm p-6",
    )


def _form_card() -> rx.Component:
    return rx.el.div(
        rx.el.form(
            rx.el.div(
                _field("Your name", "name", "Mp Kumawat"),
                _field(
                    "Email address",
                    "email",
                    "you@quiethours.press",
                    input_type="email",
                ),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
            ),
            _field("Subject", "subject", "A remark to leave in the margin"),
            _textarea(
                "Your letter", "message", "Write to us. There is no hurry."
            ),
            rx.el.div(
                rx.el.p(
                    "Every letter is read by Mp Kumawat — educator by profession, writer by nature, and the sole hand behind Qualam-e-Hayati — on Wednesdays and Sundays. Prose, Romantic-influenced poetry, original quotations, and daily thoughts are welcome at the door.",
                    class_name="font-display italic text-sm text-[#6b6558]",
                ),
                rx.el.button(
                    rx.el.span(
                        "Send letter",
                        class_name="font-mono-caps text-[0.72rem]",
                    ),
                    rx.icon("send", size=14),
                    type="submit",
                    class_name="inline-flex items-center gap-3 bg-[#244a3c] text-[#fbf7ec] px-7 py-3.5 rounded-sm hover:bg-[#1f4033] transition-all duration-500 hover:gap-4",
                ),
                class_name="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 mt-2",
            ),
            on_submit=ContactState.submit,
            reset_on_submit=True,
        ),
        class_name="paper-card rounded-sm p-8 md:p-10",
    )


def _thank_you_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("mail-check", size=32, class_name="text-[#244a3c]"),
            class_name="w-16 h-16 flex items-center justify-center rounded-full border border-[#b08b3f] bg-[#fbf7ec] mb-6 mx-auto",
        ),
        rx.el.h3(
            "Your letter is in the box.",
            class_name="font-display text-3xl md:text-4xl text-[#1f2422] mb-3 text-center",
        ),
        rx.el.p(
            f"Thank you, {ContactState.submitted_name}. Mp Kumawat reads correspondence on Wednesdays and Sundays; a reply will find you soon.",
            class_name="font-display italic text-lg text-[#4a4a44] text-center mb-8 max-w-md mx-auto",
        ),
        rx.el.div(
            rx.el.button(
                "Write another letter",
                on_click=ContactState.reset_form,
                class_name="font-mono-caps text-[0.72rem] border border-[#1f2422] text-[#1f2422] px-6 py-3 rounded-sm hover:bg-[#1f2422] hover:text-[#fbf7ec] transition-all duration-500",
            ),
            class_name="text-center",
        ),
        class_name="paper-card rounded-sm p-10 md:p-14 animate-gentle",
    )


def contact_page() -> rx.Component:
    return layout(
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    "Correspondence",
                    class_name="font-mono-caps text-[0.7rem] text-[#b08b3f] mb-6 animate-fade-rise",
                ),
                rx.el.h1(
                    "Write to the journal.",
                    class_name="font-display text-5xl md:text-6xl lg:text-7xl leading-[1.05] text-[#1f2422] mb-6 animate-fade-rise delay-100",
                ),
                rx.el.div(
                    class_name="ornament block animate-fade-rise delay-200"
                ),
                rx.el.p(
                    "Submissions, notes, corrections, or a small remark for the margin — the letterbox is open. Mp Kumawat, a literature educator and Head of Department, reads each letter as an educator by profession and writer by nature.",
                    class_name="font-display italic text-lg md:text-xl text-[#4a4a44] max-w-2xl mt-6 animate-fade-rise delay-300",
                ),
                class_name="max-w-5xl mx-auto",
            ),
            class_name="px-6 lg:px-10 pt-20 pb-14 md:pt-28",
        ),
        rx.el.section(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.cond(
                            ContactState.submitted,
                            _thank_you_card(),
                            _form_card(),
                        ),
                        class_name="lg:col-span-2",
                    ),
                    rx.el.div(
                        _info_card(
                            "mail",
                            "General correspondence",
                            "Every letter reaches Mp Kumawat directly — there is no larger desk behind this one.",
                            "letters@qalam-e-hayati.press",
                        ),
                        _info_card(
                            "feather",
                            "Submissions",
                            "Prose, poetry, translations, quotations, and daily thoughts. Read personally by Mp Kumawat — please include a short cover note and, where relevant, a little about the classroom or place from which the work comes.",
                            "submissions@qalam-e-hayati.press",
                        ),
                        _info_card(
                            "user-round",
                            "The one hand behind the lamp",
                            "Qualam-e-Hayati is written, edited, and kept by Mp Kumawat alone — an educator by profession, a writer by nature, and a literature educator and Head of Department whose journey leads from the classrooms of Rajasthan toward an American literary magazine.",
                            "Sole editor & author",
                        ),
                        class_name="flex flex-col gap-5",
                    ),
                    class_name="grid grid-cols-1 lg:grid-cols-3 gap-8",
                ),
                class_name="max-w-6xl mx-auto px-6 lg:px-10",
            ),
            class_name="pb-24",
        ),
    )
