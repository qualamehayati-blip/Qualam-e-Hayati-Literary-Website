import reflex as rx


class NavState(rx.State):
    mobile_open: bool = False

    @rx.event
    def toggle_mobile(self):
        self.mobile_open = not self.mobile_open

    @rx.event
    def close_mobile(self):
        self.mobile_open = False
