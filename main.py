import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

app = ttkb.Window(title="My Application", themename="pulse")
app.geometry("1700x900")

# Create top bar
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


# Top bar elements
logo = ttkb.Label(bar, text="Logo", bootstyle="inverse-primary")
logo.place(width=250, height=50)

searchbox = ttkb.Label(bar, text="searchbox", bootstyle="inverse-primary")
searchbox.place(x=900, width=250, height=50)

userDropDown = ttkb.Label(bar, text="userDropDown", bootstyle="inverse-primary")
userDropDown.place(x=1550, width=250, height=50)

# Menu elements with their corresponding buttons and active labels
menu_buttons = [
    ("Home", home_page, 0),
    ("Tables", tables_page, 100),
    ("Charts", charts_page, 200),
    ("Forms", forms_page, 300),
    ("Buttons", buttons_page, 400),
    ("Modals", modals_page, 500)
]

for text, page_function, y_pos in menu_buttons:
    button = ttkb.Button(menu, text=text, bootstyle="primary",
                         command=lambda pf=page_function, al=text: change_active_label_and_page(active_labels[al], pf))
    button.place(x=10, y=y_pos, width=250, height=100)

    active_label = ttkb.Label(menu, text="", bootstyle="inverse-primary")
    active_label.place(x=1, y=y_pos, width=5, height=100)
    active_labels[text] = active_label

# Initialize the first page
change_active_label_and_page(active_labels["Home"], home_page)

app.mainloop()
