import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

app = ttkb.Window(title="My Application", themename="pulse")
app.geometry("1700x900")

# Create top bar-
bar = ttkb.Frame(app, padding=10, bootstyle="primary")
bar.place(width=1700, height=70)

# Create side menu
menu = ttkb.Frame(app, padding=10, bootstyle="primary")
menu.place(y=70, width=250, height=900)

# Create main frame
main = ttkb.Frame(app, padding=10)
main.place(x=250, y=70, width=1450, height=900)

# Initialize the active_labels dictionary
active_labels = {}


# Function to change the active label and page
def change_active_label_and_page(active_label, page_function):
    for label in active_labels.values():
        label.configure(bootstyle="inverse-primary")

    active_label.configure(bootstyle="primary")
    clear_main_frame()
    page_function()


def clear_main_frame():
    for widget in main.winfo_children():
        widget.destroy()


# Page functions
def home_page():
    demo_label = ttkb.Label(main, text="HOME", bootstyle="inverse-secondary")
    demo_label.place(x=350, y=250, width=300, height=300)


def tables_page():
    demo_label = ttkb.Label(main, text="TABLES", bootstyle="inverse-secondary")
    demo_label.place(x=350, y=250, width=300, height=300)


def charts_page():
    demo_label = ttkb.Label(main, text="CHARTS", bootstyle="inverse-secondary")
    demo_label.place(x=350, y=250, width=300, height=300)


def forms_page():
    demo_label = ttkb.Label(main, text="FORMS", bootstyle="inverse-secondary")
    demo_label.place(x=350, y=250, width=300, height=300)


def buttons_page():
    demo_label = ttkb.Label(main, text="BUTTONS", bootstyle="inverse-secondary")
    demo_label.place(x=350, y=250, width=300, height=300)


def modals_page():
    demo_label = ttkb.Label(main, text="MODALS", bootstyle="inverse-secondary")
    demo_label.place(x=350, y=250, width=300, height=300)


# Toggle menu function
menu_expanded = True


def toggle_menu():
    global menu_expanded
    if menu_expanded:
        menu.place_forget()
        menu.place(y=70, width=0, height=900)
        toggle_button.configure(text="☰")
        for i, (button, label) in enumerate(menu_buttons):
            button.place_forget()
            button.place(x=10, y=i * 100, width=40, height=100)
            label.place_forget()
            label.place(x=1, y=i * 100, width=5, height=100)
    else:
        menu.place_forget()
        menu.place(y=70, width=250, height=900)
        toggle_button.configure(text="X")
        for i, (button, label) in enumerate(menu_buttons):
            button.place_forget()
            button.place(x=10, y=i * 100, width=250, height=100)
            label.place_forget()
            label.place(x=1, y=i * 100, width=5, height=100)
    menu_expanded = not menu_expanded


# Top bar elements
logo = ttkb.Label(bar, text="Logo", bootstyle="inverse-primary")
logo.place(width=250, height=50)

searchbox = ttkb.Label(bar, text="searchbox", bootstyle="inverse-primary")
searchbox.place(x=900, width=250, height=50)

userDropDown = ttkb.Label(bar, text="userDropDown", bootstyle="inverse-primary")
userDropDown.place(x=1550, width=250, height=50)

toggle_button = ttkb.Button(bar, text="X", bootstyle="primary", command=toggle_menu)
toggle_button.place(x=0, width=50, height=50)

# Menu elements with their corresponding buttons and active labels
menu_buttons = [
    (ttkb.Button(menu, text="Home", bootstyle="primary",
                 command=lambda: change_active_label_and_page(active_labels["Home"], home_page)),
     ttkb.Label(menu, text="", bootstyle="inverse-primary")),
    (ttkb.Button(menu, text="Tables", bootstyle="primary",
                 command=lambda: change_active_label_and_page(active_labels["Tables"], tables_page)),
     ttkb.Label(menu, text="", bootstyle="inverse-primary")),
    (ttkb.Button(menu, text="Charts", bootstyle="primary",
                 command=lambda: change_active_label_and_page(active_labels["Charts"], charts_page)),
     ttkb.Label(menu, text="", bootstyle="inverse-primary")),
    (ttkb.Button(menu, text="Forms", bootstyle="primary",
                 command=lambda: change_active_label_and_page(active_labels["Forms"], forms_page)),
     ttkb.Label(menu, text="", bootstyle="inverse-primary")),
    (ttkb.Button(menu, text="Buttons", bootstyle="primary",
                 command=lambda: change_active_label_and_page(active_labels["Buttons"], buttons_page)),
     ttkb.Label(menu, text="", bootstyle="inverse-primary")),
    (ttkb.Button(menu, text="Modals", bootstyle="primary",
                 command=lambda: change_active_label_and_page(active_labels["Modals"], modals_page)),
     ttkb.Label(menu, text="", bootstyle="inverse-primary")),
]

for i, (button, label) in enumerate(menu_buttons):
    button.place(x=10, y=i * 100, width=250, height=100)
    label.place(x=1, y=i * 100, width=5, height=100)
    active_labels[button.cget("text")] = label

# Initialize the first page
change_active_label_and_page(active_labels["Home"], home_page)

app.mainloop()
