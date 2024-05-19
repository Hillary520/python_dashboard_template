import ttkbootstrap as ttkb
from ttkbootstrap.constants import *


class HomePage(ttkb.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.create_cards()

    def create_cards(self):
        card_style = {
            "padding": 20,
            "bootstyle": "light",
            "borderwidth": 1,
            "relief": "solid",
        }

        self.cards = []

        # Card 1 - New Clients
        self.new_clients_card = ttkb.Frame(self, **card_style)
        self.new_clients_card.place(x=50, y=50, width=300, height=150)
        self.new_clients_label = ttkb.Label(self.new_clients_card, text="New Clients", font=("Helvetica", 16),bootstyle="primary")
        self.new_clients_label.pack()
        self.new_clients_value = ttkb.Label(self.new_clients_card, text="10", font=("Helvetica", 48),bootstyle="primary")
        self.new_clients_value.pack()
        self.cards.append(self.new_clients_card)

        # Card 2 - Orders
        self.orders_card = ttkb.Frame(self, **card_style)
        self.orders_card.place(x=400, y=50, width=300, height=150)
        self.orders_label = ttkb.Label(self.orders_card, text="Orders", font=("Helvetica", 16),bootstyle="primary")
        self.orders_label.pack()
        self.orders_value = ttkb.Label(self.orders_card, text="25", font=("Helvetica", 48),bootstyle="primary")
        self.orders_value.pack()
        self.cards.append(self.orders_card)

        # Card 3 - Sales
        self.sales_card = ttkb.Frame(self, **card_style)
        self.sales_card.place(x=750, y=50, width=300, height=150)
        self.sales_label = ttkb.Label(self.sales_card, text="Sales", font=("Helvetica", 16),bootstyle="primary")
        self.sales_label.pack()
        self.sales_value = ttkb.Label(self.sales_card, text="$1500", font=("Helvetica", 48),bootstyle="primary")
        self.sales_value.pack()
        self.cards.append(self.sales_card)

        # Card 4 - Invoices
        self.invoices_card = ttkb.Frame(self, **card_style)
        self.invoices_card.place(x=1100, y=50, width=300, height=150)
        self.invoices_label = ttkb.Label(self.invoices_card, text="Invoices", font=("Helvetica", 16),bootstyle="primary")
        self.invoices_label.pack()
        self.invoices_value = ttkb.Label(self.invoices_card, text="5", font=("Helvetica", 48),bootstyle="primary")
        self.invoices_value.pack()
        self.cards.append(self.invoices_card)

        # Apply hover effect
        for card in self.cards:
            card.bind("<Enter>", self.on_enter)
            card.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.configure(borderwidth=2, relief="raised")
        event.widget.place_configure(width=310, height=160)

    def on_leave(self, event):
        event.widget.configure(borderwidth=1, relief="solid")
        event.widget.place_configure(width=300, height=150)
