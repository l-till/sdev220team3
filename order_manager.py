class CustomerInfo:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="x", pady=10)

        self.name_label = ttk.Label(self.frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = ttk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.table_label = ttk.Label(self.frame, text="Table Number:")
        self.table_label.grid(row=1, column=0, padx=5, pady=5)
        self.table_entry = ttk.Entry(self.frame)
        self.table_entry.grid(row=1, column=1, padx=5, pady=5)

    def get_name(self):
        return self.name_entry.get()

    def get_table(self):
        return self.table_entry.get()
class OrderManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Order Manager")
        
        self.tree = ttk.Treeview(self.frame, columns=("Seat", "Item", "Price"), show="headings")
        self.tree.heading("Seat", text="Seat")
        self.tree.heading("Item", text="Item")
        self.tree.heading("Price", text="Price")
        self.tree.column("Seat", width=50)
        self.tree.column("Item", width=150)
        self.tree.column("Price", width=80)
        self.tree.grid(row=0, column=0, sticky="nsew", pady=(10, 0))

        self.total_label = ttk.Label(self.frame, text="Total: $0.00", font=('Arial', 12, 'bold'))
        
        self.label = Label(root, textvariable=self.order_status)
        self.label.pack(pady=20)
        
        self.place_order_button = Button(root, text="Place Order", command=self.place_order)
        self.place_order_button.pack(pady=10)

    def place_order(self):
        # Simulate placing an order
        self.order_status.set("Order placed successfully!")
        messagebox.showinfo("Order Status", "Your order has been placed.")