import reflex as rx


class ContactState(rx.State):
    submitted: bool = False
    submitted_name: str = ""

    @rx.event
    def submit(self, form_data: dict):
        self.submitted_name = str(form_data.get("name", "") or "reader")
        self.submitted = True
        return rx.toast(
            f"Thank you, {self.submitted_name}. Your letter has been received.",
            duration=4000,
        )

    @rx.event
    def reset_form(self):
        self.submitted = False
        self.submitted_name = ""
