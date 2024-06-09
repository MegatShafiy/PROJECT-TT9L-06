import tkinter as tk
from tkinter import messagebox, ttk
import random
import sqlite3 
import tkinter.ttk as ttk
from tkinter.ttk import Separator

class CheckIN:
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        pad = 3
        self.root.title("CHECK IN")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))


        self.conn = sqlite3.connect('Hotel.db')
        self.create_widgets()

    def create_widgets(self):
        # generate random room number
        room_number = random.randint(1, 200)

        # room Number Label
        self.room_label = tk.Label(self.root, text=f"Room Number: {room_number}", font=('Times', 16, 'bold'))
        self.room_label.pack(pady=10)

        # Name Label and Entry
        self.name_label = tk.Label(self.root, text="ENTER YOUR NAME:", font=('Times', 12, 'bold'))
        self.name_label.pack()

        self.name_entry = tk.Entry(self.root, font=('Times', 12))
        self.name_entry.pack()

        # Address Label and Entry
        self.address_label = tk.Label(self.root, text="ENTER YOUR ADDRESS:", font=('Times', 12, 'bold'))
        self.address_label.pack()

        self.address_entry = tk.Entry(self.root, font=('Times', 12))
        self.address_entry.pack()

        # Mobile Label and Entry
        self.mobile_label = tk.Label(self.root, text="ENTER YOUR MOBILE NUMBER:", font=('Times', 12, 'bold'))
        self.mobile_label.pack()

        self.mobile_entry = tk.Entry(self.root, font=('Times', 12))
        self.mobile_entry.pack()

        # Days Label and Entry
        self.days_label = tk.Label(self.root, text="ENTER NUMBER OF DAYS TO STAY:", font=('Times', 12, 'bold'))
        self.days_label.pack()

        self.days_entry = tk.Entry(self.root, font=('Times', 12))
        self.days_entry.pack()

        # Submit Button
        self.submit_button = tk.Button(self.root, text="SUBMIT", font=('Times', 12, 'bold'), command=self.submit_info)
        self.submit_button.pack(pady=20)

        # Separator
        separator = ttk.Separator(self.root, orient='horizontal')
        separator.pack(fill='x', pady=20)

        # Table
        self.table = ttk.Treeview(self.root, columns=('Fullname', 'Address', 'mobile_number', 'number_days', 'room_number'), show='headings')
        self.table.heading('Fullname', text='Fullname')
        self.table.heading('Address', text='Address')
        self.table.heading('mobile_number', text='Mobile Number')
        self.table.heading('number_days', text='Number of Days')
        self.table.heading('room_number', text='Room Number')
        self.table.pack(padx=10, pady=10)

    def submit_info(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        mobile = self.mobile_entry.get()
        days = self.days_entry.get()

        if not (name and address and mobile and days):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Add data to the SQLite database
        cursor = self.conn.cursor()
        cursor.execute('''INSERT INTO Hotel (Fullname, Address, mobile_number, number_days, room_number) 
                          VALUES (?, ?, ?, ?, ?)''', (name, address, mobile, days, random.randint(1, 200)))

        self.conn.commit()

        # Add data to the table widget
        row_id = len(self.table.get_children()) + 1
        self.table.insert('', 'end', values=(name, address, mobile, days, row_id))

        # Clear entry fields
        self.name_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.mobile_entry.delete(0, 'end')
        self.days_entry.delete(0, 'end')

        # Show success message
        messagebox.showinfo("Success", "Check-in Successfully!")

    def return_to_main_page(self):
        self.root.destroy()  # Close the CheckIN window
        self.main_window.deiconify()  # Show the main window

    def save_to_excel(self):
        # Optional: save data to Excel if needed
        pass

def check_in_ui_fun():
    root = tk.Tk()
    main_window = tk.Toplevel(root)
    main_window.title("Main Page")
    application = CheckIN(root, main_window)
    root.mainloop()
















