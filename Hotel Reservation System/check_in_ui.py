import tkinter as tk
from tkinter import messagebox, ttk
import random
import openpyxl
import main

class CheckIN:
    def __init__(self, root):
        self.root = root
        self.root.title("CHECK IN")

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Widgets
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

        # Room Type Selection
        self.room_type_label = tk.Label(self.root, text="SELECT ROOM TYPE:")
        self.room_type_label.pack()

        self.room_type_var = tk.StringVar(self.root)
        self.room_type_var.set("Select")  # Default value

        self.room_type_options = ["Single", "Double", "Suite"]  # Example room types
        self.room_type_menu = tk.OptionMenu(self.root, self.room_type_var, *self.room_type_options)
        self.room_type_menu.pack()

        # Submit Button
        self.submit_button = tk.Button(self.root, text="SUBMIT", command=self.submit_info)
        self.submit_button.pack()

        # Table
        self.table = ttk.Treeview(self.root, columns=('Name', 'Address', 'Mobile Number', 'Number of Days', 'Room Type'))
        self.table.heading('#0', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text='Address')
        self.table.heading('Mobile Number', text='Mobile Number')
        self.table.heading('Number of Days', text='Number of Days')
        self.table.heading('Room Type', text='Room Type')
        self.table.pack()

    def submit_info(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        mobile = self.mobile_entry.get()
        days = self.days_entry.get()
        room_type = self.room_type_var.get()

        if not (name and address and mobile and days and room_type):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Clear entry fields
        self.name_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.mobile_entry.delete(0, 'end')
        self.days_entry.delete(0, 'end')

    def save_to_excel(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['ID', 'Name', 'Address', 'Mobile Number', 'Number of Days', 'Room Type'])

        for item in self.table.get_children():
            values = self.table.item(item, 'values')
            ws.append([item, *values])

        wb.save('CheckInData.xlsx')

def check_in_ui_fun():
    root = tk.Tk()
    application = CheckIN(root)
    root.mainloop()
