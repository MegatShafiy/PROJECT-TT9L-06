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

        left = Frame(self.root, bg="#c9c1a7")
        left.pack(side="left", fill="both", expand=True, padx=20, pady=20)

        right = Frame(self.root, bg="#c9c1a7")
        right.pack(side="right", fill="both", expand=True)

        bottom = Frame(self.root, bg="#c9c1a7")
        bottom.pack(side="bottom", fill="x")

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

        self.back_button = Button(bottom, text="BACK", font=('Times New Roman', 20, 'bold'), bg="#725700", relief=RAISED, height=2, width=20, fg="#ffe9a1", anchor="center", command=self.go_back)
        self.back_button.pack(pady=10)

    def create_room_type_selection(self, parent):
        for idx, (room_type, description, image_path) in enumerate(self.room_types):
            frame = Frame(parent, bg="#c9c1a7", relief="solid", bd=2)
            frame.pack(fill="x", padx=10, pady=5)

            try:
                # Load and resize the image
                image = Image.open(image_path)
                image = image.resize((100, 100), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image)

                # Add the image reference to the list to prevent garbage collection
                self.image_refs.append(photo)
                
                # Display the room type name and description
                label_desc = Label(frame, font=('Times New Roman', 16), text=f"{room_type}: {description}", fg="#725700", anchor="w", bg="#c9c1a7", padx=10, pady=5)
                label_desc.pack(side="left")

                # Add the image to the frame
                image_label = Label(frame, image=photo, bg="#c9c1a7")
                image_label.image = photo  # Keep a reference to avoid garbage collection
                image_label.pack(side="right", padx=10)
            except Exception as e:
                print(f"Error loading image {image_path}: {e}")

    def go_back(self):
        self.root.destroy()
        main.home_ui()

def room_type_ui():
    root = Tk()
    app = RoomType(root)
    root.mainloop()

# Run the application
room_type_ui()
