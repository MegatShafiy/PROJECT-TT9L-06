import tkinter as tk
from tkinter import messagebox, ttk
import random
import sqlite3
from tkinter.ttk import Separator

class CheckIN:
    def __init__(self, root, main_window):
        self.root = root
        self.main_window = main_window
        pad = 3
        self.root.title("CHECK IN")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.configure(bg="#c9c1a7")  # Light brown background

        # Connect to SQLite database
        self.conn = sqlite3.connect('Hotel.db')
        self.create_table_if_not_exists()  # Ensure table exists
        self.create_widgets()

    def create_table_if_not_exists(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS Hotel (
                            Fullname TEXT,
                            Address TEXT,
                            mobile_number TEXT,
                            number_days TEXT,
                            room_number INTEGER)''')
        self.conn.commit()

        # Check if new columns exist, if not, add them
        cursor.execute("PRAGMA table_info(Hotel)")
        columns = [info[1] for info in cursor.fetchall()]
        if "room_type" not in columns:
            cursor.execute("ALTER TABLE Hotel ADD COLUMN room_type TEXT")
        if "guests" not in columns:
            cursor.execute("ALTER TABLE Hotel ADD COLUMN guests INTEGER")
        self.conn.commit()

    def create_widgets(self):
        # Main frame to hold all widgets
        main_frame = tk.Frame(self.root, bg="#c9c1a7")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Room Number
        self.room_number = random.randint(1, 200)
        self.room_label = tk.Label(main_frame, text=f"Room Number: {self.room_number}", font=('Times', 16, 'bold'), bg="#c9c1a7", fg="#725700")
        self.room_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")

        # Name
        self.name_label = tk.Label(main_frame, text="ENTER YOUR NAME:", font=('Times', 12, 'bold'), bg="#c9c1a7", fg="#725700")
        self.name_label.grid(row=1, column=0, pady=5, sticky="e")
        self.name_entry = tk.Entry(main_frame, font=('Times', 12))
        self.name_entry.grid(row=1, column=1, pady=5, sticky="w")

        # Address
        self.address_label = tk.Label(main_frame, text="ENTER YOUR ADDRESS:", font=('Times', 12, 'bold'), bg="#c9c1a7", fg="#725700")
        self.address_label.grid(row=2, column=0, pady=5, sticky="e")
        self.address_entry = tk.Entry(main_frame, font=('Times', 12))
        self.address_entry.grid(row=2, column=1, pady=5, sticky="w")

        # Mobile
        self.mobile_label = tk.Label(main_frame, text="ENTER YOUR MOBILE NUMBER:", font=('Times', 12, 'bold'), bg="#c9c1a7", fg="#725700")
        self.mobile_label.grid(row=3, column=0, pady=5, sticky="e")
        self.mobile_entry = tk.Entry(main_frame, font=('Times', 12))
        self.mobile_entry.grid(row=3, column=1, pady=5, sticky="w")

        # Days
        self.days_label = tk.Label(main_frame, text="ENTER NUMBER OF DAYS TO STAY:", font=('Times', 12, 'bold'), bg="#c9c1a7", fg="#725700")
        self.days_label.grid(row=4, column=0, pady=5, sticky="e")
        self.days_entry = tk.Entry(main_frame, font=('Times', 12))
        self.days_entry.grid(row=4, column=1, pady=5, sticky="w")

        # Room Type
        self.room_type_label = tk.Label(main_frame, text="SELECT ROOM TYPE:", font=('Times', 12, 'bold'), bg="#c9c1a7", fg="#725700")
        self.room_type_label.grid(row=5, column=0, pady=5, sticky="e")
        self.room_type = ttk.Combobox(main_frame, values=["Single", "Double", "Suite"], font=('Times', 12))
        self.room_type.grid(row=5, column=1, pady=5, sticky="w")

        # Number of Guests
        self.guests_label = tk.Label(main_frame, text="NUMBER OF GUESTS:", font=('Times', 12, 'bold'), bg="#c9c1a7", fg="#725700")
        self.guests_label.grid(row=6, column=0, pady=5, sticky="e")
        self.guests_spinbox = tk.Spinbox(main_frame, from_=1, to=10, font=('Times', 12))
        self.guests_spinbox.grid(row=6, column=1, pady=5, sticky="w")

        # Submit Button
        self.submit_button = tk.Button(main_frame, text="SUBMIT", font=('Times', 12, 'bold'), command=self.submit_info, bg="#725700", fg="#ffe9a1")
        self.submit_button.grid(row=7, column=0, columnspan=2, pady=20)

        # Separator
        separator = Separator(main_frame, orient='horizontal')
        separator.grid(row=8, column=0, columnspan=2, sticky='ew', pady=20)

        # Table Frame
        table_frame = tk.Frame(main_frame, bg="#c9c1a7")
        table_frame.grid(row=9, column=0, columnspan=2, sticky="nsew")

        # Table
        self.table = ttk.Treeview(table_frame, columns=('Fullname', 'Address', 'mobile_number', 'number_days', 'room_number', 'room_type', 'guests'), show='headings')
        self.table.heading('Fullname', text='Fullname')
        self.table.heading('Address', text='Address')
        self.table.heading('mobile_number', text='Mobile Number')
        self.table.heading('number_days', text='Number of Days')
        self.table.heading('room_number', text='Room Number')
        self.table.heading('room_type', text='Room Type')
        self.table.heading('guests', text='Guests')
        self.table.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def submit_info(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        mobile = self.mobile_entry.get()
        days = self.days_entry.get()
        room_type = self.room_type.get()
        guests = self.guests_spinbox.get()

        if not (name and address and mobile and days and room_type and guests):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            # Add data to the SQLite database
            cursor = self.conn.cursor()
            cursor.execute('''INSERT INTO Hotel (Fullname, Address, mobile_number, number_days, room_number, room_type, guests) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)''', (name, address, mobile, days, self.room_number, room_type, guests))
            self.conn.commit()

            # Add data to the table widget
            self.table.insert('', 'end', values=(name, address, mobile, days, self.room_number, room_type, guests))

            # Clear entry fields
            self.name_entry.delete(0, 'end')
            self.address_entry.delete(0, 'end')
            self.mobile_entry.delete(0, 'end')
            self.days_entry.delete(0, 'end')
            self.room_type.set('')
            self.guests_spinbox.delete(0, 'end')
            self.guests_spinbox.insert(0, 1)  # Reset to default value

            # Show success message
            messagebox.showinfo("Success", "Check-in Successful!")

            self.return_to_main_page()

        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))

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
























