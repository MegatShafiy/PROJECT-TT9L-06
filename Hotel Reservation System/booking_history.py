import sqlite3
from tkinter import *

# Function to fetch booking history from the database
def fetch_booking_history():
    conn = sqlite3.connect('Hotel.db')  # Connect to the database
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT room_number, checkin_date, checkout_date FROM Bookings')  # Query all bookings
        bookings = cursor.fetchall()
        return bookings
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        conn.close()  # Ensure the connection is closed

# Function to display booking history in the UI
def display_booking_history():
    bookings = fetch_booking_history()
    if bookings:
        for booking in bookings:
            room_number, checkin_date, checkout_date = booking
            history_list.insert(END, f"Room {room_number}: Check-in: {checkin_date}, Check-out: {checkout_date}")
    else:
        history_list.insert(END, "No booking history available.")

# Function to create the booking history UI
def booking_history_ui():
    history_window = Toplevel()
    history_window.title("Booking History")
    history_window.geometry("600x400")
    history_window.configure(bg="#c9c1a7")

    Label(history_window, text="Booking History", font=('Times', 25, 'bold'), bg="#c9c1a7", fg="#725700").pack(pady=20)

    history_list = Listbox(history_window, font=('Times', 15))
    history_list.pack(fill=BOTH, expand=True, padx=20, pady=20)

    display_booking_history()

# Example call to booking_history_ui to test it independently
if __name__ == "__main__":
    root = Tk()
    root.withdraw()  # Hide the root window
    booking_history_ui()
    root.mainloop()