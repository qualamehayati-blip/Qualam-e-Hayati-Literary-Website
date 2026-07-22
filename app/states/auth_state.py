import hashlib
import hmac
import logging
import os

import reflex as rx


_ADMIN_USERNAME_ENV = "QEH_ADMIN_USERNAME"
_ADMIN_PASSWORD_ENV = "QEH_ADMIN_PASSWORD"
_ADMIN_PASSWORD_HASH_ENV = "QEH_ADMIN_PASSWORD_HASH"
_SANDBOX_USERNAME = "admin"
_SANDBOX_PASSWORD = "hayati-admin"


class AuthState(rx.State):
    """Session-scoped admin authentication.

    Login is required for every admin route. There is no public
    registration and no visitor account system — this is a private,
    editor-only gate for the journal.
    """

    is_authenticated: bool = False
    login_error: str = ""
    login_feedback: str = ""
    submitting: bool = False

    @rx.event
    def login(self, form_data: dict):
        self.submitting = True
        self.login_error = ""
        self.login_feedback = ""
        self.is_authenticated = False
        try:
            username = str(form_data.get("username", "")).strip()
            password = str(form_data.get("password", ""))
            configured_username = os.getenv(_ADMIN_USERNAME_ENV, "").strip()
            configured_hash = (
                os.getenv(_ADMIN_PASSWORD_HASH_ENV, "").strip().lower()
            )
            configured_password = os.getenv(_ADMIN_PASSWORD_ENV, "")

            has_environment_credentials = bool(
                configured_username and (configured_hash or configured_password)
            )
            has_partial_environment_credentials = bool(
                configured_username or configured_hash or configured_password
            )
            if has_environment_credentials:
                if not configured_hash:
                    configured_hash = hashlib.sha256(
                        configured_password.encode("utf-8")
                    ).hexdigest()
                expected_username = configured_username
                fallback_active = False
            elif has_partial_environment_credentials:
                self.submitting = False
                self.login_error = (
                    "Editorial access is not configured correctly. Set the editor "
                    "username and password hash, then try again."
                )
                return
            else:
                expected_username = _SANDBOX_USERNAME
                configured_hash = hashlib.sha256(
                    _SANDBOX_PASSWORD.encode("utf-8")
                ).hexdigest()
                fallback_active = True

            password_hash = hashlib.sha256(password.encode("utf-8")).hexdigest()
            valid_username = hmac.compare_digest(username, expected_username)
            valid_password = hmac.compare_digest(password_hash, configured_hash)
            if valid_username and valid_password:
                self.is_authenticated = True
                self.submitting = False
                self.login_feedback = (
                    "Signed in with the sandbox editor account. Opening the desk…"
                    if fallback_active
                    else "Signed in. Opening the editorial desk…"
                )
                return [
                    rx.toast(
                        "Welcome back to the editorial desk.", duration=2200
                    ),
                    rx.redirect("/admin"),
                ]

            self.submitting = False
            self.login_error = "Those credentials are not correct."
        except Exception as e:
            logging.exception(f"Login error: {e}")
            self.is_authenticated = False
            self.submitting = False
            self.login_error = "Unable to sign in right now. Please try again."

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.login_error = ""
        self.login_feedback = ""
        return [
            rx.toast("Signed out. The lamp has been dimmed.", duration=2000),
            rx.redirect("/admin/login"),
        ]

    @rx.event
    def require_auth(self):
        """Redirect to login when a protected admin page is opened."""
        if not self.is_authenticated:
            return rx.redirect("/admin/login")

    @rx.event
    def redirect_if_authenticated(self):
        """When already signed in, skip the login page."""
        if self.is_authenticated:
            return rx.redirect("/admin")
