import sqlite3
from tkinter import *
from tkinter import messagebox

# Function to check room availability
def check_availability(checkin_date, checkout_date):
    conn = sqlite3.connect('Hotel.db')  # Connect to the database
    try:
        cursor = conn.cursor()
        
        # Fetch available rooms for the selected period
        cursor.execute('''
            SELECT room_number 
            FROM Rooms 
            WHERE room_number NOT IN (
                SELECT room_number 
                FROM Bookings 
                WHERE checkin_date <= ? AND checkout_date >= ?
            )
        ''', (checkout_date, checkin_date))
        available_rooms = cursor.fetchall()
        
        # Fetch availability dates for the selected period
        cursor.execute('''
            SELECT DISTINCT checkin_date, checkout_date 
            FROM Bookings 
            WHERE checkin_date >= ? AND checkout_date <= ?
        ''', (checkin_date, checkout_date))
        availability_dates = cursor.fetchall()
        
        return available_rooms, availability_dates
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return [], []
    finally:
        conn.close()

# Function to handle button click
def on_check_availability_click():
    checkin_date = checkin_entry.get()
    checkout_date = checkout_entry.get()
    if checkin_date and checkout_date:
        available_rooms, availability_dates = check_availability(checkin_date, checkout_date)
        if available_rooms:
            rooms_str = ", ".join([str(room[0]) for room in available_rooms])
            dates_str = "\n".join([f"Available from {date[0]} to {date[1]}" for date in availability_dates])
            messagebox.showinfo("Available Rooms", f"Available rooms: {rooms_str}\n\n{dates_str}")
        else:
            messagebox.showinfo("No Rooms Available", "No rooms available for the selected dates.")
    else:
        messagebox.showwarning("Empty Fields", "Please enter both check-in and check-out dates.")

# Create availability UI
availability_window = Tk()
availability_window.title("Check Room Availability")
availability_window.geometry("400x300")
availability_window.configure(bg="#c9c1a7")

Label(availability_window, text="Enter Check-in Date (YYYY-MM-DD):", font=('Times', 15), bg="#c9c1a7", fg="#725700").pack(pady=10)
checkin_entry = Entry(availability_window, font=('Times', 15))
checkin_entry.pack(pady=10)

Label(availability_window, text="Enter Check-out Date (YYYY-MM-DD):", font=('Times', 15), bg="#c9c1a7", fg="#725700").pack(pady=10)
checkout_entry = Entry(availability_window, font=('Times', 15))
checkout_entry.pack(pady=10)

Button(availability_window, text="Check Availability", font=('Times', 15), bg="#948363", fg="#ffe9a1", command=on_check_availability_click).pack(pady=20)

availability_window.mainloop()
