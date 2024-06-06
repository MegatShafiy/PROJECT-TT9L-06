from tkinter import *
from tkinter import messagebox

def check_availability(checkin_date, checkout_date):
    conn = sqlite3.connect('Hotel.db')  # Connect to the database
    try:
        cursor = conn.cursor()
        # Replace this query with actual logic to check room availability based on dates
        cursor.execute('SELECT room_number FROM Bookings WHERE checkin_date <= ? AND checkout_date >= ?', (checkout_date, checkin_date))
        available_rooms = cursor.fetchall()
        return [str(room[0]) for room in available_rooms]
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return []
    finally:
        conn.close()  # Ensure the connection is closed

    