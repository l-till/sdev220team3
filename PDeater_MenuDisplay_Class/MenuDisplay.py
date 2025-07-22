"""
Paul Deater
7/14/25
Framwork for MenuDisplay class
"""

import tkinter as tk
from tkinter import *


class MenuDisplay:
    def __init__(self, root):
        self.root = root
        self.menu = {
            'Appetizers': [
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

 
root = tk.Tk()
root.title("Test window")
root.geometry("900x900") 
x = MenuDisplay(root)
x.CreateMenu()
root.mainloop()