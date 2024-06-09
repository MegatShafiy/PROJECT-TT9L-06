import tkinter as tk
import sqlite3

def room_availability_ui():
    root = tk.Tk()
    root.title("ROOM AVAILABILITY")

    table = ttk.Treeview(root, columns=('Room Number', 'Room Type', 'Is Available'))
    table.heading('#0', text='ID')
    table.heading('Room Number', text='Room Number')
    table.heading('Room Type', text='Room Type')
    table.heading('Is Available', text='Is Available')
    table.pack()

    conn = sqlite3.connect('Hotel.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM RoomAvailability")
    rooms = cursor.fetchall()
    for i, room in enumerate(rooms):
        table.insert('', 'end', text=i + 1, values=room)
    conn.close()

    root.mainloop()