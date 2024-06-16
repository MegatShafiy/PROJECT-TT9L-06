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