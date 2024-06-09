import tkinter as tk
from tkinter import messagebox, ttk
import openpyxl
import main
from room_availability import room_availability_ui
import sqlite3
from datetime import datetime

class CheckIN:
    def __init__(self, root):
        self.root = root
        self.root.title("CHECK IN")

        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self.root, text="ENTER YOUR NAME:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.address_label = tk.Label(self.root, text="ENTER YOUR ADDRESS:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack()

        self.mobile_label = tk.Label(self.root, text="ENTER YOUR MOBILE NUMBER:")
        self.mobile_label.pack()
        self.mobile_entry = tk.Entry(self.root)
        self.mobile_entry.pack()

        self.days_label = tk.Label(self.root, text="ENTER NUMBER OF DAYS TO STAY:")
        self.days_label.pack()
        self.days_entry = tk.Entry(self.root)
        self.days_entry.pack()

        self.room_type_label = tk.Label(self.root, text="SELECT ROOM TYPE:")
        self.room_type_label.pack()
        self.room_type_var = tk.StringVar(self.root)
        self.room_type_var.set("Select")
        self.room_type_options = ["Single", "Double", "Suite"]
        self.room_type_menu = tk.OptionMenu(self.root, self.room_type_var, *self.room_type_options)
        self.room_type_menu.pack()

        self.room_availability_button = tk.Button(self.root, text="CHECK ROOM AVAILABILITY", command=self.check_room_availability)
        self.room_availability_button.pack()

        self.submit_button = tk.Button(self.root, text="SUBMIT", command=self.submit_info)
        self.submit_button.pack()

        self.table = ttk.Treeview(self.root, columns=('Name', 'Address', 'Mobile Number', 'Number of Days', 'Room Type', 'Room Number'))
        self.table.heading('#0', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text='Address')
        self.table.heading('Mobile Number', text='Mobile Number')
        self.table.heading('Number of Days', text='Number of Days')
        self.table.heading('Room Type', text='Room Type')
        self.table.heading('Room Number', text='Room Number')
        self.table.pack()

    def submit_info(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        mobile = self.mobile_entry.get()
        days = self.days_entry.get()
        room_type = self.room_type_var.get()

        if not (name and address and mobile and days and room_type != "Select"):
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        # Add data to the table
        row_id = len(self.table.get_children()) + 1
        room_number = random.randint(100, 999)  # Randomly assign a room number for simplicity
        self.table.insert('', 'end', text=row_id, values=(name, address, mobile, days, room_type, room_number))
        
        
        
        
