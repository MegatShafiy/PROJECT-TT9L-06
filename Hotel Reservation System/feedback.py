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

        