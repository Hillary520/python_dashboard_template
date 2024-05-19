import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


class UserDropDown(ttkb.Frame):
    def __init__(self, master, theme, **kwargs):
        super().__init__(master, **kwargs)

        # Store the theme name
        self.theme = theme

        # Configure frame
        self.configure(bootstyle="primary")
        self.place(x=1550, y=70, width=150, height=150)

        # Add buttons
        self.settings_button = ttkb.Button(self, text="Settings", bootstyle="secondary", command=self.settings)
        self.settings_button.pack(fill=BOTH, expand=True, padx=10, pady=5)

        self.profile_button = ttkb.Button(self, text="Profile", bootstyle="secondary", command=self.profile)
        self.profile_button.pack(fill=BOTH, expand=True, padx=10, pady=5)

        self.logout_button = ttkb.Button(self, text="Logout", bootstyle="danger", command=self.logout)
        self.logout_button.pack(fill=BOTH, expand=True, padx=10, pady=5)

        # Initially hide the drop-down
        self.place_forget()

    def settings(self):
        print("Settings button clicked")

    def profile(self):
        print("Profile button clicked")

    def logout(self):
        print("Logout button clicked")

    def toggle(self):
        if self.winfo_ismapped():
            self.place_forget()
        else:
            self.place(x=1550, y=70, width=150, height=150)

    def update_theme(self, theme):
        self.theme = theme
        # Update the bootstyle of each button to reflect the new theme
        self.settings_button.configure(bootstyle="secondary")
        self.profile_button.configure(bootstyle="secondary")
        self.logout_button.configure(bootstyle="danger")
        self.configure(bootstyle="info")
