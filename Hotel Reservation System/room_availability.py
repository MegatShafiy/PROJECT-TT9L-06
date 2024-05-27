from tkinter import *
from tkinter import messagebox

def check_availability_ui():
    availability_window = Toplevel()
    availability_window.title("Check Room Availability")
    availability_window.geometry("400x300")
    availability_window.configure(bg="#c9c1a7")

    Label(availability_window, text="Enter Check-in Date (YYYY-MM-DD):", font=('Times', 15), bg="#c9c1a7", fg="#725700").pack(pady=10)
    checkin_entry = Entry(availability_window, font=('Times', 15))
    checkin_entry.pack(pady=10)

    Label(availability_window, text="Enter Check-out Date (YYYY-MM-DD):", font=('Times', 15), bg="#c9c1a7", fg="#725700").pack(pady=10)
    checkout_entry = Entry(availability_window, font=('Times', 15))
    checkout_entry.pack(pady=10)

    def check_availability():
        checkin_date = checkin_entry.get()
        checkout_date = checkout_entry.get()
        available_rooms = ["101", "102", "103"]  # Replace with actual room availability check
        messagebox.showinfo("Available Rooms", f"Available rooms from {checkin_date} to {checkout_date}: {', '.join(available_rooms)}")

    Button(availability_window, text="Check Availability", font=('Times', 15), bg="#948363", fg="#ffe9a1", command=check_availability).pack(pady=20)
