"""
Paul Deater
7/14/25
Framework for MenuDisplay class
"""

import tkinter as tk
from tkinter import *


class MenuDisplay:
    def __init__(self, root):
        self.root = root
        #self.
        self.menu = {
            'Appetizers': [
                {'Name': 'Spring Rolls', 'price': 5.99},
            {'Name': 'Garlic Bread', 'price': 4.99},
            {'Name': 'Bruschetta', 'price': 6.99},
            {'Name': 'Calamari', 'price': 8.99},
            {'Name': 'Stuffed Mushrooms', 'price': 7.99},
            {'Name': 'Buffalo Wings', 'price': 9.99},
            {'Name': 'Nachos', 'price': 8.49},
            {'Name': 'Onion Rings', 'price': 5.49},
            {'Name': 'Mozzarella Sticks', 'price': 6.49},
            {'Name': 'Potato Skins', 'price': 7.49},
                ],

            'Appetizers2': [
                {'Name':"nachos", 'Price': 12.99}
                ],

            'Appetizers3': [
                {'Name':"nachos", 'Price': 12.99}
                ],

            'Drinks': [
                {'Name':"Tea", 'Price': 3.49}
                    ]
        }
    """
    Will create the menu items within a frame
    along with a button to modify the menu
    """
    def CreateMenu(self,row_position,column_position,manager_status):
        self.first_iteration = True
        self.menu_frame = tk.Frame(root, bg="lightblue", width=500, height=100)
        self.menu_frame.grid(row = row_position, column = column_position)
        # menu_frame.grid_propagate(0)
        

        section_frame = tk.Frame(self.menu_frame, bg="lightblue")
        section_frame.grid(row=0, column=0, padx=5, pady=5)

        for section in self.menu.keys():
            section_button = tk.Button(section_frame, text = section, command = lambda open_section = section: self.populate_section(open_section), bg="seashell3")
            section_button.pack(side=TOP, expand=True)


        self.populate_section(list(self.menu.keys())[0])

        if manager_status:
            edit_menu_button = tk.Button(self.menu_frame,text=f"Edit Menu",command= self.UpdateItem)
            edit_menu_button.grid(row=1, column=1)


    
    def populate_section(self, section):
        if self.first_iteration:
            self.detail_frame = tk.Frame(self.menu_frame,bg="lightblue")
            self.detail_frame.grid(row=0, column=1)
            self.first_iteration = False

        if self.detail_frame.winfo_exists():
            for detail_listed in self.detail_frame.winfo_children():
                detail_listed.destroy()
        

        position_on_x = 0
        position_on_y = 1

        menu_data = self.menu[section]

        for main_key, sub_key in enumerate(menu_data):
            # Creates muli-line string - Must not be indented
            button_text = f"""{str(sub_key['Name'])} 
{str(sub_key['price'])}"""
            
            button = tk.Button(self.detail_frame,text = button_text, bg="seashell3",height=2,width=15,command = lambda entry = button_text: self.AddItem(entry))
            button.grid(row=position_on_x, column=position_on_y,padx=6,pady=6)

            position_on_y += 1
            if position_on_y > 3:
                position_on_y = 1
                position_on_x +=1



    """
    This function is for when an item has been clicked
    It will add the pressed item to the order
    """
    def AddItem(name,price):
        print(name, price)

    """
    This function is for when the modify menu button has been clicked.
    It allows a user with acces to modify menu items; add, remove, or update.
    """
    def UpdateItem():
        pass

 
root = tk.Tk()
root.title("Test window")
root.geometry("900x900") 
x = MenuDisplay(root)
x.CreateMenu(2,0,True)
root.mainloop()