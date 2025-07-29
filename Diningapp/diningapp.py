"""
Bryce Harrison
7/16/25
Diningapp class - A ttk.Frame for managing dining tables and seat selection.

"""


import tkinter as tk
from tkinter import ttk

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
        self["padding"] = 20

        style.configure("Unoccupied.TButton", background="green", foreground="black")
        style.configure("Selected.TButton", background="red", foreground="black")

        title_label = ttk.Label(self, text="Table Selection", font=("Helvetica", 14, "bold"))
        title_label.grid(row=0, column=0, pady=(10, 20))

        table_frame = ttk.Frame(self, padding=10, relief="ridge", borderwidth=2)
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
        
        btn = self.tables[table_name]
        btn.configure(style="Selected.TButton")

    def toggle_seat(self, table_name, seat_number, var):
        if var.get():
            if seat_number not in self.selected_seats[table_name]:
                self.selected_seats[table_name].append(seat_number)
                print(f"{table_name} - Seat {seat_number} selected.")
                if self.on_table_select:
                    self.on_table_select(table_name=table_name, seat_number=seat_number, selected=True)
        else:
            if seat_number in self.selected_seats[table_name]:
                self.selected_seats[table_name].remove(seat_number)
                print(f"{table_name} - Seat {seat_number} deselected.")
                if self.on_table_select:
                    self.on_table_select(table_name=table_name, seat_number=seat_number, selected=False)

# === test ===
if __name__ == "__main__":
    def handle_selection(table_name, seat_number, selected):
        print(f"[OrderManager] Table: {table_name}, Seat: {seat_number}, Selected: {selected}")

    root = tk.Tk()
    root.title("Table Selection")
    root.geometry("640x420")

    frame = Diningapp(root, on_table_select=handle_selection)
    frame.pack(padx=20, pady=20)

    root.mainloop()