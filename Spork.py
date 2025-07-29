# Spork App
# Last change 2025-07-29

# import necessary libraries
import tkinter as tk
from tkinter import ttk, Label, Button, StringVar, messagebox
from tkinter.font import Font

# ----- Login Screen -----
# 2025-07-28
class LoginScreen(ttk.Frame):

   VALID_USERS = {
      "111222": "Logan",
      "112212": "Bryce",
      "121212": "Paul",
   }

   def __init__(self, root, on_login_success):
      super().__init__(root)
      self.root = root
      self.on_login_success = on_login_success
      self.user_id = StringVar()
      self.pack(fill="both", expand=True)

      ttk.Label(self, text="Enter Your 6-digit ID", font=("Arial", 18)).pack(pady=10)

      self.display = ttk.Entry(self, textvariable=self.user_id, font=("Arial", 20), justify="center", width=10, state="readonly")
      self.display.pack(pady=10)

      pad_frame = ttk.Frame(self)
      pad_frame.pack()

      buttons = [
         ('1', '2', '3'),
         ('4', '5', '6'),
         ('7', '8', '9'),
         ('Clear', '0', 'Del')
      ]

      for r, row in enumerate(buttons):
         for c, char in enumerate(row):
            tk.Button(pad_frame, text=char, font=("Arial", 16), width=5, height=2,
                     command=lambda ch=char: self.on_button_click(ch)).grid(row=r, column=c, padx=5, pady=5)

      tk.Button(self, text="Login", font=("Arial", 16), width=10, command=self.validate_login).pack(pady=10)

   def on_button_click(self, char):
      current = self.user_id.get()
      if char == 'Clear':
         self.user_id.set("")
      elif char == 'Del':
         self.user_id.set(current[:-1])
      elif char.isdigit():
         if len(current) < 6:
            self.user_id.set(current + char)

   def validate_login(self):
      uid = self.user_id.get()
      if uid in self.VALID_USERS:
         name = self.VALID_USERS[uid]
         self.destroy()
         self.on_login_success(uid, name)
      else:
         messagebox.showerror("Login Failed", "Invalid User ID.")

# ----- TableMap Class -----
# 2025-07-28
class TableMap(ttk.Frame):
   def __init__(self, parent, on_table_select, on_logout):
      super().__init__(parent)
      self.parent = parent
      self.on_table_select = on_table_select
      self.on_logout = on_logout

      self.grid(row=0, column=0, sticky="nsew")
      parent.grid_rowconfigure(0, weight=1)
      parent.grid_columnconfigure(0, weight=1)

      self.create_widgets()

   def create_widgets(self):
      style = ttk.Style()
      style.theme_use('clam')
      self["padding"] = 20

      # Ensure the frame itself expands properly
      self.grid_rowconfigure(2, weight=1)
      self.grid_columnconfigure(0, weight=1)

      # --- Header Row with Logout Button ---
      header_frame = tk.Frame(self)
      header_frame.grid(row=0, column=0, sticky="ew", columnspan=2)
      header_frame.grid_columnconfigure(0, weight=1)

      logout_btn = tk.Button(header_frame, text="Logout", command=self.logout)
      logout_btn.pack(side="right", padx=10, pady=10)

      # --- Title ---
      title_label = ttk.Label(self, text="Table Selection", font=("Helvetica", 16, "bold"))
      title_label.grid(row=1, column=0, columnspan=2, pady=(10, 20))

      # --- Table Buttons Grid ---
      table_frame = ttk.Frame(self, padding=10, relief="ridge", borderwidth=2)
      table_frame.grid(row=2, column=0, columnspan=2, sticky="nsew")

      # Ensure table_frame stretches
      self.grid_rowconfigure(2, weight=1)
      self.grid_columnconfigure(0, weight=1)
      table_frame.grid_rowconfigure("all", weight=1)
      table_frame.grid_columnconfigure("all", weight=1)

      layout = {
         "Table 1": (0, 0),
         "Table 2": (0, 2),
         "Booth 1": (1, 1),
         "Table 3": (2, 0),
         "Table 4": (2, 2),
         "Booth 2": (3, 1),
      }

      for table_name, (row, col) in layout.items():
         btn = ttk.Button(
               table_frame,
               text=table_name,
               width=15,
               command=lambda name=table_name: self.on_table_select(name)
         )
         btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
         table_frame.grid_rowconfigure(row, weight=1)
         table_frame.grid_columnconfigure(col, weight=1)

   def logout(self):
      self.destroy()
      self.on_logout()

# ----- MenuDisplay Class -----
# 2025-07-29
class MenuDisplay(ttk.Frame):
   def __init__(self, parent, on_item_click):
      super().__init__(parent, padding=10, relief="groove", borderwidth=2)
      self.on_item_click = on_item_click
      self.pack(fill="both", expand=True)
      self.menu_data = {
         'Apps': [
         {'name': 'Spring Rolls', 'price': 5.99},
         {'name': 'Garlic Bread', 'price': 4.99},
         {'name': 'Bruschetta', 'price': 6.99},
         {'name': 'Calamari', 'price': 8.99},
         {'name': 'Stuffed Mushrooms', 'price': 7.99},
         {'name': 'Buffalo Wings', 'price': 9.99},
         {'name': 'Nachos', 'price': 8.49},
         {'name': 'Onion Rings', 'price': 5.49},
         {'name': 'Mozzarella Sticks', 'price': 6.49},
         {'name': 'Potato Skins', 'price': 7.49},
         ],
         'Salads': [
         {'name': 'Caesar Salad', 'price': 8.99},
         {'name': 'Greek Salad', 'price': 9.99},
         {'name': 'Caprese Salad', 'price': 10.99},
         {'name': 'Garden Salad', 'price': 7.99},
         {'name': 'Spinach Salad', 'price': 8.99},
         {'name': 'Cobb Salad', 'price': 11.99},
         ],
         'Entrees': [
         {'name': 'Grilled Chicken', 'price': 14.99},
         {'name': 'Steak', 'price': 19.99},
         {'name': 'Salmon', 'price': 17.99},
         {'name': 'Pasta Primavera', 'price': 12.99},
         {'name': 'Vegetable Stir Fry', 'price': 11.99},
         {'name': 'Shrimp Scampi', 'price': 18.99},
         {'name': 'Beef Tacos', 'price': 10.99},
         {'name': 'Chicken Alfredo', 'price': 13.99},
         {'name': 'Lamb Chops', 'price': 22.99},
         {'name': 'Vegetable Curry', 'price': 11.49},
         ],
         'Desserts': [
         {'name': 'Cheesecake', 'price': 6.99},
         {'name': 'Chocolate Cake', 'price': 5.99},
         {'name': 'Tiramisu', 'price': 7.99},
         {'name': 'Apple Pie', 'price': 5.49},
         {'name': 'Crème Brûlée', 'price': 9.99},
         {'name': 'Chocolate Mousse', 'price': 6.99},
         ],
         'Beverages': [
         {'name': 'Soda', 'price': 2.99},
         {'name': 'Coffee', 'price': 2.49},
         {'name': 'Tea', 'price': 1.99},
         {'name': 'Juice', 'price': 3.49},
         {'name': 'Water', 'price': 0.00},
         {'name': 'Iced Tea', 'price': 2.99},
         {'name': 'Lemonade', 'price': 3.49},
         ],
         'Specials': [
         {'name': 'Lobster Tail', 'price': 29.99},
         {'name': 'Filet Mignon', 'price': 24.99},
         {'name': 'Seafood Paella', 'price': 22.99},
         {'name': 'Duck Confit', 'price': 21.99},
         {'name': 'Rack of Lamb', 'price': 26.99},
         {'name': 'Surf and Turf', 'price': 34.99},
         {'name': 'Truffle Risotto', 'price': 19.99},
         {'name': 'Osso Buco', 'price': 23.99},
         {'name': 'Beef Wellington', 'price': 28.99},
         {'name': 'Sea Bass', 'price': 24.49},
         ],
      }

      self.categoryframe = ttk.Frame(self)
      self.categoryframe.pack(fill='x', pady=(0, 10))
      for i, category in enumerate(self.menu_data.keys()):
         btn = ttk.Button(self.categoryframe, text=category, command=lambda c=category: self.CreateMenu(c))
         btn.grid(row=0, column=i, sticky='ew',padx=2)
         self.categoryframe.columnconfigure(i, weight=1)

      self.menu_frame = ttk.Frame(self)
      self.menu_frame.pack(fill='both', expand=True)

      self.CreateMenu(list(self.menu_data.keys())[0])

   
   # Will create the menu items within a frame
   def CreateMenu(self, category):
      for widget in self.menu_frame.winfo_children():
         widget.destroy()

      row, col = 0, 0
      for item in self.menu_data[category]:
         frame = ttk.Frame(self.menu_frame, padding=5, relief="solid", borderwidth=1)
         frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

         ttk.Label(frame, text=item['name'], font=('Arial', 10, 'bold')).pack()
         ttk.Label(frame, text=f"${item['price']:.2f}").pack()

         frame.bind("<Button-1>", lambda e, it=item: self.on_item_click(it))
         for child in frame.winfo_children():
               child.bind("<Button-1>", lambda e, it=item: self.on_item_click(it))

         col += 1
         if col > 2:
               col = 0
               row += 1

      for i in range(3):
         self.menu_frame.columnconfigure(i, weight=1)
      for i in range(row + 1):
         self.menu_frame.rowconfigure(i, weight=1)
   
   """
   This function is for when an item has been clicked
   It will add the pressed item to the order
   
   def AddItem(self, item):
      self.on_item_click(item)
   """

# ----- OrderManager Class -----
# 2025-07-29
class OrderManager(ttk.Frame):
   def __init__(self, parent, table_number):
      super().__init__(parent, borderwidth=2, relief="groove")
      self.pack(fill="both", expand=True)
      
      self.tree = ttk.Treeview(self.frame, columns=("Seat", "Item", "Price"), show="headings")
      self.tree.heading("Seat", text="Seat")
      self.tree.heading("Item", text="Item")
      self.tree.heading("Price", text="Price")
      self.tree.column("Seat", width=50)
      self.tree.column("Item", width=150)
      self.tree.column("Price", width=80)
      self.tree.grid(row=0, column=0, sticky="nsew", pady=(10, 0))

      self.total_label = ttk.Label(self, text="Total: $0.00", font=('Arial', 12, 'bold'))
      self.total_label.grid(row=1, column=0, pady=5)
      
      self.order_status = StringVar()
      self.order_status.set('')

      self.status_label = Label(self, textvariable=self.order_status)
      self.status_label.grid(row=2, column=0, pady=5)

      self.place_order_button = Button(self, text="Place Order", command=self.place_order)
      self.place_order_button.grid(row=3, column=0, pady=10)

      self.total = 0.0

   def add_order_item(self, name, price):
      self.tree.insert("", "end", values=("", name, f"${price:.2f}"))
      self.total += price
      self.total_label.config(text=f"Total: ${self.total:.2f}")

   def place_order(self):
      self.order_status.set("Order placed successfully!")
      messagebox.showinfo("Order Status", "Your order has been placed.")

# ----- OrderScreen Class -----
# 2025-07-29
class OrderScreen(ttk.Frame):
   def __init__(self, root, user_info, table_number, on_back):
      super().__init__(root)
      self.user_id, self.name = user_info
      self.table_number = table_number
      self.on_back = on_back
      self.pack(fill='both', expand=True)

      # Sets up the header with buttons and label
      header = ttk.Frame(self)
      header.pack(side='top', fill='x')
      header.columnconfigure(0, weight=1)
      header.columnconfigure(1, weight=2)
      header.columnconfigure(2, weight=1)

      # Back to Map Button
      back_btn = ttk.Button(header, text="Back to Map", command=self.back)
      back_btn.grid(row=0, column=0, sticky='w', padx=10, pady=10)

      # Table Number Label tied to map
      table_label = ttk.Label(header, text=f"{self.table_number}", anchor='center', font=("Arial", 16, "bold"))
      table_label.grid(row=0, column=1, sticky='nsew')

      # Logout Button
      logout_btn = ttk.Button(header, text="Logout", command=self.logout)
      logout_btn.grid(row=0, column=2, sticky='e', padx=10, pady=10)

      # Main content area
      content_frame = ttk.Frame(self)
      content_frame.pack(fill="both", expand=True, padx=10, pady=10)
      content_frame.columnconfigure(0, weight=4)
      content_frame.columnconfigure(1, weight=3)

      # Box for menu display
      left_box = ttk.Frame(content_frame)
      left_box.grid(row=1, column=0, sticky="nsew")
      self.menu_display = MenuDisplay(left_box, self.add_item_to_order)

      # Box for order management
      right_box = ttk.Frame(content_frame)
      right_box.grid(row=1, column=1, sticky="nsew")
      self.order_manager = OrderManager(right_box, self.table_number)

   def add_order_item(self, item):
      self.order_manager.add_order_item(item['name'], item['price'])

   def back(self):
      self.destroy()
      self.on_back(self.user_id, self.name)

   def logout(self):
      self.destroy()
      app.show_login_screen()

# ----- SporkApp Class -----
# 2025-07-28
class SporkApp:
   def __init__(self, root):
      self.root = root
      self.root.title('Spork')
      self.root.geometry('1280x720')
      self.root.resizable(False, False)
      self.current_table = None
      self.show_login_screen()

   def clear_window(self):
      for widget in self.root.winfo_children():
         widget.destroy()

   def show_login_screen(self):
      self.clear_window()
      LoginScreen(self.root, self.handle_login)

   def handle_login(self, user_id, name):
      self.user_info = (user_id, name)
      self.show_table_map()

   def show_table_map(self):
      self.clear_window()
      TableMap(self.root, self.show_order_screen, self.show_login_screen)

   def show_order_screen(self, table_number):
      self.clear_window()
      self.current_table = table_number
      OrderScreen(self.root, self.user_info, table_number, self.show_table_map)

if __name__ == "__main__":

   # This will print the title of the app
   print("\n***************************************")
   print("Spork (by Team 3)")
   print("***************************************\n")

   root = tk.Tk()
   app = SporkApp(root)
   root.mainloop()