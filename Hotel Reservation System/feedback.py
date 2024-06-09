from tkinter import *
from tkinter import ttk

class FeedbackPage:
    def __init__(self, root):
        self.root = root
        self.root.title("K I N G S T O N  H O T E L - FEEDBACK")
        self.root.geometry("600x400")
        self.root.configure(bg="#c9c1a7")

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title label
        self.label = Label(self.main_frame, text="Feedback", font=('Times', 30, 'bold'), fg="#725700", bg="#c9c1a7")
        self.label.pack(pady=20)

        # Name Label and Entry
        self.name_label = Label(self.main_frame, text="Name:", font=('Times', 20), fg="#725700", bg="#c9c1a7")
        self.name_label.pack(pady=5, anchor=W)
        self.name_entry = Entry(self.main_frame, font=('Times', 18), width=30)
        self.name_entry.pack(pady=5)

        