import reflex as rx
from app.states.auth_state import AuthState


def _field(
    label: str,
    name: str,
    placeholder: str,
    input_type: str = "text",
    autofocus: bool = False,
) -> rx.Component:
    return rx.el.div(
        rx.el.label(
            label,
            class_name="block font-mono-caps text-[0.62rem] text-[#6b6558] mb-2",
        ),
        rx.el.input(
            type=input_type,
            name=name,
            placeholder=placeholder,
            required=True,
            auto_focus=autofocus,
            class_name="w-full bg-[#fbf7ec] border border-[#d9cfb6] rounded-sm px-4 py-3 text-[#1f2422] font-serif-body text-[0.98rem] focus:outline-none focus:border-[#244a3c] transition-colors duration-500 placeholder:text-[#a89f8a]",
        ),
        class_name="mb-5",
    )


def admin_login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("arrow-left", size=13),
                rx.el.span(
                    "Return to the journal",
                    class_name="font-mono-caps text-[0.65rem] link-refined",
                ),
                href="/",
                class_name="inline-flex items-center gap-2 text-[#244a3c] mb-10",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "lock-keyhole",
                            size=22,
                            class_name="text-[#244a3c]",
                        ),
                        class_name="w-14 h-14 flex items-center justify-center rounded-full border border-[#d9cfb6] bg-[#fbf7ec] mx-auto mb-6",
                    ),
                    rx.el.div(
                        "Editorial Access Only",
                        class_name="font-mono-caps text-[0.65rem] text-[#b08b3f] text-center mb-3",
                    ),
                    rx.el.h1(
                        "The Editors' Door",
                        class_name="font-display text-4xl md:text-5xl text-[#1f2422] text-center mb-3",
                    ),
                    rx.el.div(class_name="ornament block text-center mb-6"),
                    rx.el.p(
                        "This gate is reserved for the journal's editors. There are no visitor accounts, and no public sign-ups — the reading rooms remain open to all.",
                        class_name="font-display italic text-[#4a4a44] text-center mb-5 text-[0.98rem] max-w-sm mx-auto",
                    ),
                    rx.el.p(
                        "Sandbox guidance: if deployment credentials have not been configured, use the private single-editor credentials provided with this app. For any public deployment, set QEH_ADMIN_USERNAME and QEH_ADMIN_PASSWORD_HASH.",
                        class_name="text-[0.78rem] text-[#6b6558] text-center leading-relaxed max-w-sm mx-auto mb-8",
                    ),
                    rx.el.form(
                        _field(
                            "Username",
                            "username",
                            "admin",
                            autofocus=True,
                        ),
                        _field(
                            "Password",
                            "password",
                            "•••••••••••",
                            input_type="password",
                        ),
                        rx.cond(
                            AuthState.login_error != "",
                            rx.el.div(
                                rx.icon(
                                    "triangle-alert",
                                    size=14,
                                    class_name="text-[#b04a3f]",
                                ),
                                rx.el.span(
                                    AuthState.login_error,
                                    class_name="text-[0.85rem] text-[#b04a3f] font-serif-body",
                                ),
                                class_name="flex items-center gap-2 mb-5 px-3 py-2 rounded-sm bg-[#f4dcd6] border border-[#e0b8ae]",
                            ),
                            rx.cond(
                                AuthState.login_feedback != "",
                                rx.el.div(
                                    rx.icon(
                                        "circle-check",
                                        size=14,
                                        class_name="text-[#244a3c]",
                                    ),
                                    rx.el.span(
                                        AuthState.login_feedback,
                                        class_name="text-[0.85rem] text-[#244a3c] font-serif-body",
                                    ),
                                    class_name="flex items-center gap-2 mb-5 px-3 py-2 rounded-sm bg-[#e2ecd6] border border-[#c9d8b8]",
                                ),
                                rx.fragment(),
                            ),
                        ),
                        rx.el.button(
                            rx.cond(
                                AuthState.submitting,
                                rx.el.span(
                                    "Signing in…",
                                    class_name="font-mono-caps text-[0.72rem]",
                                ),
                                rx.fragment(
                                    rx.el.span(
                                        "Enter the desk",
                                        class_name="font-mono-caps text-[0.72rem]",
                                    ),
                                    rx.icon("arrow-right", size=14),
                                ),
                            ),
                            type="submit",
                            disabled=AuthState.submitting,
                            class_name="w-full inline-flex items-center justify-center gap-3 bg-[#244a3c] text-[#fbf7ec] px-6 py-3.5 rounded-sm hover:bg-[#1f4033] transition-all duration-500",
                        ),
                        on_submit=AuthState.login,
                        reset_on_submit=False,
                    ),
                    rx.el.div(class_name="thin-rule mt-8 mb-6"),
                    rx.el.p(
                        "Forgot the way in? Speak to the editor in charge; there is no self-serve reset.",
                        class_name="text-center font-display italic text-[0.85rem] text-[#6b6558]",
                    ),
                    class_name="paper-card rounded-sm p-8 md:p-10 animate-gentle",
                ),
                class_name="w-full max-w-md mx-auto",
            ),
            class_name="w-full max-w-md mx-auto",
        ),
        on_mount=AuthState.redirect_if_authenticated,
        class_name="parchment-bg min-h-screen flex flex-col justify-center px-6 py-16",
    )
