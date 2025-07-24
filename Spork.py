# Spork App
# Last change 2025-07-23


# This will print the title of the app
print("\n***************************************")
print("Spork (by Team 3)")
print("***************************************\n")

# import necessary libraries
import tkinter as tk
from tkinter import ttk, Label, Button, StringVar, messagebox
from tkinter.font import Font


# Variables
order_items = []
order_total = 0.0

# ---------------- Spork App Class ----------------
# This class initializes the main application window
class SporkApp(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.root.title('Spork')
        self.root.geometry('800x600')
        self.root.resizable(False, False)

        main_frame = ttk.Frame(root, padding=10)
        main_frame.pack(fill="both", expand=True)


"""
Paul Deater
7/14/25
Framwork for MenuDisplay class
"""

class MenuDisplay:
   def __init__(self, root):
      self.root = root
      self.menu = {
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

   """
   Will create the menu items within a frame
   along with a button to modify the menu
   """
   def CreateMenu(self,row_position,column_position):
      menu_frame = tk.Frame(root, bg="lightblue", width=2000, height=100)
      menu_frame.grid(row = row_position, column = column_position, sticky='nsew')
      
      

      

      


   """
   This function is for when an item has been clicked
   It will add the pressed item to the order
   """
   def AddItem():
      pass

   """
   This function is for when the modify menu button has been clicked.
   It allows a user with acces to modify menu items; add, remove, or update.
   """
   def UpdateItem():
      pass

"""
Logan Till
7/23/25
Framework for CustomerInfo and OrderManager classes
"""

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
      self.frame = ttk.Frame(root)
      self.frame.pack(fill="both", expand=True)
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
      
      self.order_status = StringVar()
      self.order_status.set("")

      self.label = Label(root, textvariable=self.order_status)
      self.label.pack(pady=20)
      
      self.place_order_button = Button(root, text="Place Order", command=self.place_order)
      self.place_order_button.pack(pady=10)

   def place_order(self):
      # Simulate placing an order
      self.order_status.set("Order placed successfully!")
      messagebox.showinfo("Order Status", "Your order has been placed.")

if __name__ == "__main__":
   root = tk.Tk()
   app = SporkApp(root)
   root.mainloop()