from tkinter import *
from tkinter import ttk

class RoomAvailabilityPage:
    def __init__(self, root):
        self.root = root
        self.root.title("K I N G S T O N  H O T E L - ROOM AVAILABILITY")
        self.root.geometry("600x400")
        self.root.configure(bg="#c9c1a7")

        # Create main frame
        self.main_frame = Frame(self.root, bg="#c9c1a7")
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title label
        self.label = Label(self.main_frame, text="Room Availability", font=('Times', 30, 'bold'), fg="#725700", bg="#c9c1a7")
        self.label.pack(pady=20)

        # Date Label and Entry
        self.date_label = Label(self.main_frame, text="Date (YYYY-MM-DD):", font=('Times', 20), fg="#725700", bg="#c9c1a7")
        self.date_label.pack(pady=5, anchor=W)
        self.date_entry = Entry(self.main_frame, font=('Times', 18), width=20)
        self.date_entry.pack(pady=5)

        # Button styles
        self.button_style = ttk.Style()
        self.button_style.configure('Availability.TButton', font=('Times', 18), background="#948363", foreground="#ffe9a1")

        # Check Availability Button
        self.check_button = ttk.Button(self.main_frame, text="CHECK AVAILABILITY", style='Availability.TButton', command=self.check_availability)
        self.check_button.pack(pady=10)

        # Back Button
        self.back_button = ttk.Button(self.main_frame, text="BACK", style='Availability.TButton', command=self.back_to_main)
        self.back_button.pack(pady=10)

        
