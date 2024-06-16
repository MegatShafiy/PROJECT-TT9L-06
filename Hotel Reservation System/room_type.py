import sqlite3
from tkinter import *
from PIL import Image, ImageTk  # Import Pillow for image handling

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

        left = Frame(self.root, bg="#c9c1a7")
        left.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        right = Frame(self.root, bg="#c9c1a7")
        right.pack(side="right", fill="both", expand=True)

        self.label = Label(top, font=('Times New Roman', 50, 'bold'), text="ROOM TYPE", fg="#725700", anchor="center", bg="#c9c1a7")
        self.label.pack(pady=10)

        # Room type information with image paths
        self.room_types = [
            ("Single Room", "Room assigned to one person. May have one or two beds.", "singleroom.jpg"),
            ("Double Room", "Room assigned to two people. May have one or more beds.", "doubleroom.jpg"),
            ("Suite", "A set of rooms designated for a particular purpose such as a bedroom, living room, and kitchen.", "suiteroom.jpg"),
            ("Family Room", "A room with several beds, often designed for family accommodation.", "familyroom.jpg")
        ]

        self.image_refs = []  # Keep a reference to the images to prevent garbage collection

        self.create_room_type_selection(left)