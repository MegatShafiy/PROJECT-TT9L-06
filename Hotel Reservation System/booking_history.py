from tkinter import *

def booking_history_ui():
    history_window = Toplevel()
    history_window.title("Booking History")
    history_window.geometry("600x400")
    history_window.configure(bg="#c9c1a7")

    Label(history_window, text="Booking History", font=('Times', 25, 'bold'), bg="#c9c1a7", fg="#725700").pack(pady=20)

    history_list = Listbox(history_window, font=('Times', 15))
    history_list.pack(fill=BOTH, expand=True, padx=20, pady=20)

    bookings = [
        "Booking 1: Room 101, Check-in: 2023-05-01, Check-out: 2023-05-05",
        "Booking 2: Room 102, Check-in: 2023-06-10, Check-out: 2023-06-15",
    ]
    for booking in bookings:
        history_list.insert(END, booking)
