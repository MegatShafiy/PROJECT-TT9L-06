import sqlite3
from tkinter import *
import main

class RoomType:

    def __init__(self, root):
        self.root = root
        pad = 3
        self.root.title("ROOM TYPE")
        self.root.geometry(
            "{0}x{1}+0+0".format(self.root.winfo_screenwidth() - pad, self.root.winfo_screenheight() - pad))
        self.root.configure(bg="#c9c1a7")
        top = Frame(self.root, bg="#c9c1a7")
        top.pack(side="top", fill="x")

        bottom = Frame(self.root, bg="#c9c1a7")
        bottom.pack(side="bottom", fill="x")

        left = Frame(self.root, bg="#c9c1a7")
        left.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        right = Frame(self.root, bg="#c9c1a7")
        right.pack(side="right", fill="both", expand=True)


        self.label = Label(top, font=('Times New Roman', 50, 'bold'), text="ROOM TYPE", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.pack(pady=10)

        # room type information 
        self.room_types = [
            ("Single Room", "Room assigned to one person. May have one or two beds."),
            ("Double Room", "Room assigned to two people. May have one or more beds."),
            ("Suite", "A set of rooms designated for a particular purpose such as a bedroom, living room, and kitchen."),
            ("Family Room", "A room with several beds, often designed for family accommodation.")
        ]

        self.selected_room_type = StringVar()
        self.selected_room_type.set(self.room_types[0][0]) 

        self.create_room_type_selection(left)
        self.submit_button = Button(bottom, text="SUBMIT", font=('Times New Roman', 20, 'bold'), bg="#725700", relief=RAISED, height=2, width=20, fg="#ffe9a1", anchor="center", command=self.submit_selection)
        self.submit_button.pack(pady=10)

        self.back_button = Button(bottom, text="BACK", font=('Times New Roman', 20, 'bold'), bg="#725700", relief=RAISED, height=2, width=20, fg="#ffe9a1", anchor="center", command=self.go_back)
        self.back_button.pack(pady=10)

        self.remove_room_type_table()  # Remove room type table

    def create_room_type_selection(self, parent):
        for idx, (room_type, description) in enumerate(self.room_types):
            frame = Frame(parent, bg="#c9c1a7", relief="solid", bd=2)
            frame.pack(fill="x", padx=10, pady=5)

            # using radio_button to make options that can be selected

            radio_button = Radiobutton(frame, text=room_type, variable=self.selected_room_type, value=room_type, font=('Times New Roman', 20, 'bold'), bg="#c9c1a7", fg="#725700", anchor="w", padx=10, pady=5, selectcolor="white")
            radio_button.pack(side="left")

            label_desc = Label(frame, font=('Times New Roman', 16), text=description, fg="#725700", anchor="w", bg="#c9c1a7", padx=10, pady=5)
            label_desc.pack(side="right")

    def remove_room_type_table(self):
        conn = sqlite3.connect('Hotel.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('DROP TABLE IF EXISTS RoomType')
            conn.commit()

    def submit_selection(self):
        selected_room = self.selected_room_type.get()
        print(f"Selected Room Type: {selected_room}")
        self.save_room_type(selected_room)

    def save_room_type(self, room_type):
        fullname = "" 
        room_number = 101 
        conn = sqlite3.connect('Hotel.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO RoomType (Fullname, room_number, room_type) VALUES (?, ?, ?)', (fullname, room_number, room_type))
            conn.commit()

    def go_back(self):
        self.root.destroy()
        main.home_ui()

def room_type_ui():
    root = Tk()
    app = RoomType(root)
    root.mainloop()







