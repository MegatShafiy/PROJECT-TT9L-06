import tkinter as tk

def booking_history_ui_fun():
    print("Booking History UI function called")
    root = tk.Tk()
    root.title("Booking History")

    label = tk.Label(root, text="Booking History:")
    label.pack()

    # Code to fetch and display booking history from the database
    booking_list = tk.Listbox(root)
    booking_list.pack()

    # Example data, replace with actual database query
    bookings = ["Booking 1", "Booking 2", "Booking 3"]
    for booking in bookings:
        booking_list.insert(tk.END, booking)

    root.mainloop()
