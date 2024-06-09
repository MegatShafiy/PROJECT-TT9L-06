import tkinter as tk
from tkinter import messagebox, ttk
import random
import openpyxl
import main
from room_availability import room_availability_ui

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

        # Submit Button
        self.submit_button = tk.Button(self.root, text="SUBMIT", command=self.submit_info)
        self.submit_button.pack()

        # Room Availability Button
        self.room_availability_button = tk.Button(self.root, text="CHECK ROOM AVAILABILITY", command=self.check_room_availability)
        self.room_availability_button.pack()

        # Table
        self.table = ttk.Treeview(self.root, columns=('Name', 'Address', 'Mobile Number', 'Number of Days'))
        self.table.heading('#0', text='ID')
        self.table.heading('Name', text='Name')
        self.table.heading('Address', text='Address')
        self.table.heading('Mobile Number', text='Mobile Number')
        self.table.heading('Number of Days', text='Number of Days')
        self.table.pack()

    def submit_info(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        mobile = self.mobile_entry.get()
        days = self.days_entry.get()

        if not (name and address and mobile and days):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Add data to the table
        row_id = len(self.table.get_children()) + 1
        self.table.insert('', 'end', text=row_id, values=(name, address, mobile, days))

        # Clear entry fields
        self.name_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.mobile_entry.delete(0, 'end')
        self.days_entry.delete(0, 'end')

    def save_to_excel(self):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['ID', 'Name', 'Address', 'Mobile Number', 'Number of Days'])

        for item in self.table.get_children():
            values = self.table.item(item, 'values')
            ws.append([item, *values])

        wb.save('CheckInData.xlsx')

def check_in_ui_fun():
    root = tk.Tk()
    application = CheckIN(root)
    root.mainloop()
