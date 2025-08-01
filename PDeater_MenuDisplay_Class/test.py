import tkinter as tk
from tkinter import *
from tkinter import ttk, Label, Button, StringVar, messagebox


class OrderManager(ttk.Frame):
   def __init__(self,):
      self.root = root

      self.current_table = None
      self.current_seat = None

      self.right_box = ttk.Frame()
      self.right_box.grid(row=0, column=1, sticky="nsew")
      

      # Storage -- Remove if broken
      self.order_storage = {
          "Table 1": [
              {'seat': '','name': '','price': 0}
          ],
          "Table 2": [
              {'seat': '','name': '','price': 0}
          ],
          "Table 3": [
              {'seat': '','name': '','price': 0}
          ],
          "Table 4": [
              {'seat': '','name': '','price': 0}
          ],
          "Booth 1": [
              {'seat': '','name': '','price':0}
          ],
          "Booth 2": [
              {'seat': '','name': '','price': 0}
          ],
        }
      
      self.tree = ttk.Treeview(self.right_box, columns=("Seat", "Item", "Price"), show="headings")
      self.tree.heading("Seat", text="Seat")
      self.tree.heading("Item", text="Item")
      self.tree.heading("Price", text="Price")
      self.tree.column("Seat", width=50)
      self.tree.column("Item", width=150)
      self.tree.column("Price", width=80)
      self.tree.grid(row=0, column=0, sticky="nsew", pady=(10, 0))

      self.total_label = ttk.Label(self.right_box, text="Total: $0.00", font=('Arial', 12, 'bold'))
      self.total_label.grid(row=1, column=0, pady=5)
      
      self.order_status = StringVar()
      self.order_status.set('')

      self.status_label = Label(self.right_box, textvariable=self.order_status)
      self.status_label.grid(row=2, column=0, pady=5)

      self.place_order_button = Button(self.right_box, text="Place Order", command=self.place_order)
      self.place_order_button.grid(row=3, column=0, pady=10)

      self.table_label = Label(self.right_box, text=f"Active Table: {self.current_table}")
      self.table_label.grid(row=4, column=0, pady=5)

      self.seat_label = Label(self.right_box, text='')
      self.seat_label.grid(row=5, column=0, pady=5)

      self.total = 0.0

    #Paul Additions
   def set_table_or_booth(self, table_or_booth):
      if table_or_booth != self.current_table:
        self.current_table = table_or_booth

        if table_or_booth in self.order_storage:
          self.tree.delete(*self.tree.get_children())

          self.active_order_storage = self.order_storage[table_or_booth]
          self.total = 0.0

          for main_key, sub_key in enumerate(self.active_order_storage):
            #This check exists because I want order_storage to have examples of its format
            if sub_key['price'] != 0:
                self.tree.insert("", "end", values=(sub_key['seat'], sub_key['name'], f"${sub_key['price']}"))

            self.total += sub_key['price']
            self.total_label.config(text=f"Total: ${self.total:.2f}")


        self.table_label.config(text=f"Active Table: {self.current_table}")
        self.current_seat = ""
        self.seat_label.config(text="No Active Seat")
      else:
          pass

   def set_current_seat(self,table_or_booth,seat_number,select_or_deselect):
      if table_or_booth == self.current_table and select_or_deselect:

        self.current_seat = seat_number

        self.seat_label.config(text=f"Active Seat: {self.current_seat}")
      elif select_or_deselect == False:
          self.current_seat = ""
          self.seat_label.config(text="No Active Seat")
      else:
        messagebox.showwarning(title="ERROR - Seat Selected outside CurrentTable", message="Please only select seats with in the active table")

   def add_order_item(self, name, price):
      if self.current_table:
        self.tree.insert("", "end", values=(self.current_seat, name, f"${price:.2f}"))
        self.total += price
        self.total_label.config(text=f"Total: ${self.total:.2f}")

        self.active_order_storage.append({'seat': self.current_seat,'name': name,'price': price})

      else:
          messagebox.showwarning(title="ERROR - No Table Selected", message="Please select a Table")

   def place_order(self):
      self.order_status.set("Order placed successfully!")
      messagebox.showinfo("Order Status", "Your order has been placed.")


class MenuDisplay:
    def __init__(self, root, OrderManager_object):
        self.root = root

        self.class_OrderManager = OrderManager_object
    
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
    Creates the menu items within a frame, along with a button to modify the menu.
    Requires three values, the first two are for position and the third is for determining manager access.
    """
    def CreateMenu(self,row_position,column_position,manager_status):
        # Used within the populate_section() function
        self.first_iteration = True

        # Creates the base menu frame
        self.menu_frame = tk.Frame(self.root, bg="gray85",width=500, height=100)
        self.menu_frame.grid(row = row_position, column = column_position)
        
        # Creates a frame to hold buttons for choosing sections
        section_frame = tk.Frame(self.menu_frame, bg="gray85")
        section_frame.grid(row=0, column=0, padx=5, pady=5)

        # Creates the buttons for the previously mentioned frame
        for section in self.menu.keys():
            section_button = tk.Button(section_frame, text = section, command = lambda open_section = section: self.populate_section(open_section), bg="seashell3",height=1,width=10)
            section_button.pack(side=TOP, expand=True)

        # calls the function with the specified parameter -- See block comment for further details
        self.populate_section(list(self.menu.keys())[0])

        #Creates a button for modifying the menu if True -- See UpdateItem() for explanation
        extract_status = manager_status[2]
        if extract_status:
            edit_menu_button = tk.Button(self.menu_frame,height=1,width=12,text=f"Edit Menu",command= self.UpdateItem)
            edit_menu_button.grid(row=1, column=1)



    def populate_section(self, section):
        if self.first_iteration:
            self.detail_frame = tk.Frame(self.menu_frame,bg="gray85",width=375, height=215)
            self.detail_frame.grid(row=0, column=1)
            self.detail_frame.grid_propagate(False)
            self.first_iteration = False

        if self.detail_frame.winfo_exists():
            for detail_listed in self.detail_frame.winfo_children():
                detail_listed.destroy()
        

        position_on_x = 0
        position_on_y = 1

        menu_data = self.menu[section]

        for main_key, sub_key in enumerate(menu_data):

        # Creates multi-line string -- Must not be indented
            button_text = f"""{str(sub_key['name'])} 
{str(sub_key['price'])}"""
            
            #formats values into a list
            button_output = (sub_key['name'], sub_key['price'])

            button = tk.Button(self.detail_frame,text = button_text,  bg="seashell3",height=2,width=15,command = lambda entry = button_output: self.AddItem(entry))
            button.grid(row=position_on_x, column=position_on_y,padx=6,pady=6)

            #Sets the positioning of the buttons, creating new rows as necessary
            position_on_y += 1
            if position_on_y > 3:
                position_on_y = 1
                position_on_x +=1



    """
    This function is for when an item has been clicked
    It will add the pressed item to the order
    """
    def AddItem(self,entry):
        name = entry[0]
        price = entry[1]
        self.class_OrderManager.add_order_item(name, price)

    """
    This function is for when the modify menu button has been clicked.
    It allows a user with access to modify menu items; add, remove, or update.
    """
    def UpdateItem(self):
        # cretes a new window
        self.modify_menu_window = Toplevel(bg="lightblue")
        # sets the title
        self.modify_menu_window.title('Menu Modify Screen')
        # sets the windows size
        self.modify_menu_window.geometry("600x600")

        modify_section_frame = tk.Frame(self.modify_menu_window, bg="green")
        modify_section_frame.grid(row=0, column=0, padx=5, pady=5)

        # Creates the buttons for the previously mentioned frame
        for section in self.menu.keys():
            section_button = tk.Button(modify_section_frame, text = section, command = lambda open_section = section: self.populate_modify_section(open_section), bg="seashell3")
            section_button.pack(side=BOTTOM, expand=True)

        self.detail_listbox = Listbox(modify_section_frame, height=7,width=25)
        self.detail_listbox.pack(side=RIGHT, fill=BOTH)

        self.detail_scrollbar = Scrollbar(modify_section_frame)
        self.detail_scrollbar.pack(side=RIGHT, fill=BOTH)
        self.detail_listbox.config(yscrollcommand=self.detail_scrollbar.set)

        self.populate_modify_section(list(self.menu.keys())[0])



    def populate_modify_section(self, current_section):

        menu_data = self.menu[current_section]
        
        self.detail_listbox.delete(0,tk.END)

        for main_key, sub_key in enumerate(menu_data):
            # Creates a string 
            button_text = f"""{str(sub_key['name'])} - {str(sub_key['price'])}"""
            self.detail_listbox.insert(tk.END,button_text)
 

class Diningapp(ttk.Frame):
    def __init__(self, parent, on_table_select=None):
        super().__init__(parent)
        self.parent = parent
        self.on_table_select = on_table_select 
        self.tables = {}  
        self.occupied = set()  
        self.selected_seats = {}  
        self.seat_vars = {}

        self.create_widgets()

    def create_widgets(self):
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Arial", 10))
        style.configure("TCheckbutton", font=("Arial", 9))
        self.configure(style="TFrame")
        self["padding"] = 5

        style.configure("Unoccupied.TButton", background="green", foreground="black")
        style.configure("Selected.TButton", background="red", foreground="black")

        title_label = ttk.Label(self, text="Table Selection", font=("Helvetica", 14, "bold"))
        title_label.grid(row=0, column=0, pady=(5, 10))

        table_frame = ttk.Frame(self, padding=5, relief="ridge", borderwidth=2)
        table_frame.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        table_frame.rowconfigure("all", weight=1)
        table_frame.columnconfigure("all", weight=1)

        layout = {
            "Table 1": (0, 0),
            "Table 2": (0, 2),
            "Booth 1": (1, 1),
            "Table 3": (2, 0),
            "Table 4": (2, 2),
            "Booth 2": (3, 1),
        }

        for table_name, (row, col) in layout.items():
            table_container = ttk.Frame(table_frame)
            table_container.grid(row=row, column=col, padx=8, pady=8)
            table_container.columnconfigure(0, weight=1)
            table_container.columnconfigure(1, weight=1)
            table_container.grid_propagate(True)

            
            if "Booth" in table_name:
                seat_count = 2
            else:
                seat_count = 4

            self.selected_seats[table_name] = []

            if seat_count == 4:
                
                btn = ttk.Button(
                    table_container,
                    text=table_name,
                    style="Unoccupied.TButton",
                    command=lambda t=table_name: self.select_table(t)
                )
                btn.grid(row=1, column=1, pady=(2, 4), sticky="nsew")
                self.tables[table_name] = btn

                seat_positions = {
                    0: (0, 0),  
                    1: (0, 2),  
                    2: (2, 0),  
                    3: (2, 2),  
                }
                
                for idx in range(3):
                    table_container.rowconfigure(idx, weight=1)
                    table_container.columnconfigure(idx, weight=1)
                for i in range(4):
                    var = tk.IntVar()
                    cb = ttk.Checkbutton(
                        table_container,
                        variable=var,
                        text=f"{i+1}",
                        command=lambda t=table_name, s=i+1, v=var: self.toggle_seat(t, s, v)
                    )
                    r, c = seat_positions[i]
                    cb.grid(row=r, column=c, padx=2, pady=1, sticky="nsew")
                    self.seat_vars[(table_name, i+1)] = var
            else:
                
                btn = ttk.Button(
                    table_container,
                    text=table_name,
                    style="Unoccupied.TButton",
                    command=lambda t=table_name: self.select_table(t)
                )
                btn.grid(row=0, column=0, columnspan=2, pady=(2, 4), sticky="nsew")
                self.tables[table_name] = btn
                for i in range(seat_count):
                    var = tk.IntVar()
                    cb = ttk.Checkbutton(
                        table_container,
                        variable=var,
                        text=f"{i+1}",
                        command=lambda t=table_name, s=i+1, v=var: self.toggle_seat(t, s, v)
                    )
                    r = (i // 2) + 1  
                    c = (i % 2)
                    cb.grid(row=r, column=c, padx=2, pady=1, sticky="nsew")
                    self.seat_vars[(table_name, i+1)] = var

    def select_table(self, table_name):
        self.on_table_select.set_table_or_booth(table_name)

    def toggle_seat(self, table_name, seat_number, var):
        if var.get():
            if seat_number not in self.selected_seats[table_name]:
                self.selected_seats[table_name].append(seat_number)
                #print(f"{table_name} - Seat {seat_number} selected.")
                self.on_table_select.set_current_seat(table_name,seat_number,True)
                #if self.on_table_select:
                 #   self.on_table_select(table_name=table_name, seat_number=seat_number, selected=True)
        else:
            if seat_number in self.selected_seats[table_name]:
                self.selected_seats[table_name].remove(seat_number)
                #print(f"{table_name} - Seat {seat_number} deselected.")
                self.on_table_select.set_current_seat(table_name,seat_number,False)
                #if self.on_table_select:
                 #   self.on_table_select(table_name=table_name, seat_number=seat_number, selected=False)


class LoginScreen(ttk.Frame):

   VALID_USERS = {
      "111222": ["Logan",True],
      "112212": ["Bryce",False],
      "121212": ["Paul",True],
   }

   def __init__(self, root,on_login_success):
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
         uid_values = self.VALID_USERS[uid]
         name = uid_values[0]
         permision = uid_values[1]
         self.destroy()
         self.on_login_success(uid, name,permision)
      else:
         messagebox.showerror("Login Failed", "Invalid User ID.")




root = tk.Tk()
root.title("Test window")
root.geometry("1280x720") 
root.configure(bg="gray85")


def you_logged_in(user_info):
    for widget in root.winfo_children():
        widget.destroy()

    OrderManager()
    OrderManager_object = OrderManager()


    frame = Diningapp(root, OrderManager_object)
    frame.grid(row=0,column=0,padx=10,pady=10)


    x = MenuDisplay(root, OrderManager_object)
    x.CreateMenu(1,1,user_info)


    user_info_frame = tk.Frame(root, bg="gray85",width=500, height=100)
    user_info_frame.grid(row = 1, column = 0)

    if user_info[2]:
        tk.Label(user_info_frame,text= f"** Manager View **", font=("Arial", 16)).pack(pady=5)

    tk.Label(user_info_frame,text= f"Name - {user_info[1]}", font=("Arial", 16)).pack(pady=5)
    tk.Label(user_info_frame,text= f"User ID - {user_info[0]}", font=("Arial", 16)).pack(pady=5)
    

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

def show_login_screen():
    clear_window()
    LoginScreen(root, handle_login)

def handle_login(user_id, name, permision):
    user_info = [user_id, name, permision]
    you_logged_in(user_info)


show_login_screen()


root.mainloop()