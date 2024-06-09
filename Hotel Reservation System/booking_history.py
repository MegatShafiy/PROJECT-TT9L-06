import tkinter as tk
from tkinter import messagebox, ttk
import openpyxl
import main
from room_availability import room_availability_ui
import sqlite3
from datetime import datetime

class BookingHistoryPage:
    def __init__(self, root):
        self.root = root
        self.root.title("K I N G S T O N  H O T E L - BOOKING HISTORY")
        self.root.geometry("800x600")
        self.root.configure(bg="#c9c1a7")

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title label
        self.label = Label(self.main_frame, text="Booking History", font=('Times', 30, 'bold'), fg="#725700", bg="#c9c1a7")
        self.label.pack(pady=20)

        # Treeview for displaying booking history
        self.tree = ttk.Treeview(self.main_frame, columns=("Booking ID", "Customer Name", "Room Number", "Check-in Date", "Check-out Date"), show="headings")
        self.tree.heading("Booking ID", text="Booking ID")
        self.tree.heading("Customer Name", text="Customer Name")
        self.tree.heading("Room Number", text="Room Number")
        self.tree.heading("Check-in Date", text="Check-in Date")
        self.tree.heading("Check-out Date", text="Check-out Date")
        self.tree.pack(fill=BOTH, expand=True)

        # Back Button
        self.back_button = ttk.Button(self.main_frame, text="BACK", command=self.back_to_main)
        self.back_button.pack(pady=10)

        # Load booking history
        self.load_booking_history()

    def load_booking_history(self):
        booking_history = self.get_booking_history()

        for booking in booking_history:
            self.tree.insert("", END, values=booking)

    def get_booking_history(self):
        # Dummy data for demonstration purposes
        # Replace this with actual logic to fetch booking history
        dummy_data = [
            (1, "John Doe", 101, "2024-06-01", "2024-06-05"),
            (2, "Jane Smith", 102, "2024-06-03", "2024-06-07"),
            (3, "Alice Johnson", 103, "2024-06-02", "2024-06-06"),
        ]
        return dummy_data

    def back_to_main(self):
        self.root.destroy()

def booking_history_ui():
    history_root = Tk()
    app = BookingHistoryPage(history_root)
    history_root.mainloop()


        
        
        
        
