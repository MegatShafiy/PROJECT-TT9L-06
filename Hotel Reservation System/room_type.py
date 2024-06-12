import sqlite3
from tkinter import *
from PIL import Image, ImageTk  # Import Pillow for image handling
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

         # room type information with image paths
        self.room_types = [
            ("Single Room", "Room assigned to one person. May have one or two beds.", "single_room.jpg"),
            ("Double Room", "Room assigned to two people. May have one or more beds.", "double_room.jpg"),
            ("Suite", "A set of rooms designated for a particular purpose such as a bedroom, living room, and kitchen.", "suite.jpg"),
            ("Family Room", "A room with several beds, often designed for family accommodation.", "family_room.jpg")
        ]

        self.selected_room_type = StringVar()
        self.selected_room_type.set(self.room_types[0][0]) 

        self.create_room_type_selection(left)
        self.submit_button = Button(bottom, text="SUBMIT", font=('Times New Roman', 20, 'bold'), bg="#725700", relief=RAISED, height=2, width=20, fg="#ffe9a1", anchor="center", command=self.submit_selection)
        self.submit_button.pack(pady=10)

        self.back_button = Button(bottom, text="BACK", font=('Times New Roman', 20, 'bold'), bg="#725700", relief=RAISED, height=2, width=20, fg="#ffe9a1", anchor="center", command=self.go_back)
        self.back_button.pack(pady=10)

        self.remove_room_type_table()  # Remove room type table








